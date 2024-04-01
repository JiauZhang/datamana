import os, pickle, signal, sys
from multiprocessing.managers import BaseManager
from multiprocessing.shared_memory import SharedMemory
from queue import Queue

queue = Queue()
class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue', callable=lambda:queue)
m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')

meta_data = {
    'pid': os.getpid(),
}
print(meta_data)
meta_data_pkl = pickle.dumps(meta_data)

# shm = SharedMemory(name='_internal_meta_data', create=True, size=len(meta_data_pkl))

def abrt_handler(signalnum, frame):
    print('abrt_handler...')
    m.shutdown()
    sys.exit(0)

signal.signal(signal.SIGTERM, abrt_handler)

s = m.get_server()
s.serve_forever()
