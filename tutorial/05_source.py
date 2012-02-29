import zmq
import numpy as np
from pickle import loads, dumps
import time

ctx = zmq.Context()
size = 1024

push = ctx.socket(zmq.PUSH)
push.bind('tcp://127.0.0.1:1501')

i = 0

while True:
    s = np.random.rand(size)
    print "Sending signal:", i
    push.send_multipart([s,dumps(s.shape),dumps(s.dtype)])
    # We need to throttle the rate so downstream is not flooded.
    time.sleep(1.0)
    i += 1
