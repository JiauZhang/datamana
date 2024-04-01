import time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue')
m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
m.connect()
queue = m.get_queue()

count = 0
while True:
    print(count)
    queue.put(count)
    count += 1
    time.sleep(1)