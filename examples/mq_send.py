import time, os
from datamana.core import MQueue

mq = MQueue()
errno = mq.open('/datamana-01', os.O_CREAT, 666)
if errno != 0:
    print(f'MQueue open failed! <{os.strerror(errno)}>')
    exit(-1)
