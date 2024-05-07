import time, os
from datamana._C import MQueue

mq = MQueue()
mq.flags = 0
mq.msgsize = 8
mq.maxmsg = 4
errno = mq.open('/datamana', os.O_CREAT | os.O_RDWR, 600)
if errno != 0:
    print(f'MQueue open failed! <{os.strerror(errno)}>')
    exit(-1)
count = 0
pid = os.getpid()

while count < 20:
    msg = 'hello'
    print(f'<{pid}>send msg: {msg}')
    mq.send(msg, 0)
    count += 1
    time.sleep(1)
