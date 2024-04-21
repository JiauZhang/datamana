import time, os
from datamana.core import MQueue

mq = MQueue()
mq.flags = 0
mq.msgsize = 1
mq.maxmsg = 4
errno = mq.open('/datamana-01', os.O_CREAT, 666)
if errno != 0:
    print(f'MQueue open failed! <{os.strerror(errno)}>')
    exit(-1)
