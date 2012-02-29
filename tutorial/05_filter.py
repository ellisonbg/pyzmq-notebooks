import zmq
import numpy as np
from pickle import loads, dumps

ctx = zmq.Context()
size = 1024
window_size = 128

pull = ctx.socket(zmq.PULL)
pull.connect('tcp://127.0.0.1:1501')
push = ctx.socket(zmq.PUSH)
push.connect('tcp://127.0.0.1:1502')

i = 0

while True:
    msg_list = pull.recv_multipart()
    buf = msg_list[0]
    shape = loads(msg_list[1])
    dtype = loads(msg_list[2])
    s = np.frombuffer(buf, dtype=dtype).reshape(shape)
    print "Processing signal: ", i
    w = np.hamming(window_size)
    s = np.r_[s[window_size-1:0:-1],s,s[-1:-window_size:-1]]
    ss = np.convolve(w/w.sum(),s,mode='valid')
    push.send_multipart([ss,dumps(ss.shape),dumps(ss.dtype)])
    i += 1
