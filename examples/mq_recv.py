import os
from datamana.ipc import MQueue

mq = MQueue('datamana', msgsize=8, maxmsg=4)
count = 0
pid = os.getpid()

while count < 20:
    ret, msg, msg_prio = mq.receive()
    print(f'<{pid}>receive msg: {ret, msg, msg_prio}')
    count += 1