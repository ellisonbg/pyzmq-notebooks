import sys
import zmq

port = sys.argv[1]

ctx = zmq.Context()
rep = ctx.socket(zmq.REP)
rep.bind('tcp://127.0.0.1:%s' % port)
while True:
    s = rep.recv()
    print "Reversing:", s
    rep.send(s[::-1])

