import pickle, time
from multiprocessing import shared_memory, managers

share_name = 'server_share_data'
torch_name = 'server_torch_data'

shared_shm = shared_memory.SharedMemory(share_name)
torch_shm = shared_memory.SharedMemory(torch_name)

shared_data = pickle.loads(shared_shm.buf)
address = shared_data['address']
authkey = shared_data['authkey']

SyncManager = managers.SyncManager
SyncManager.register('next')

manager = SyncManager(address=address, authkey=authkey)
manager.connect()

for _ in range(20):
    manager.next()
    data = pickle.loads(torch_shm.buf)
    print(data)
