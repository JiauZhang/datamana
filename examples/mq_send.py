import time, os
from datamana.ipc import MQueue

mq = MQueue('datamana', msgsize=8, maxmsg=4)
count = 0
pid = os.getpid()

while count < 20:
    msg = 'hello'
    print(f'<{pid}>send msg: {msg}')
    mq.send(msg, 0)
    count += 1
    time.sleep(1)
