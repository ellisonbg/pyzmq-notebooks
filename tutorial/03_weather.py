import sys
import time
import zmq
from random import choice

cities = ['new york','seattle','austin','miami','los angeles','san francisco','chicago']
conditions = ['sunny','foggy','snowing','cloudy','raining']

port = sys.argv[1]
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://127.0.0.1:%s'%port)

while True:
    pub.send_multipart([choice(cities),choice(conditions)])
    time.sleep(0.5)

 