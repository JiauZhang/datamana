import os, pickle
from multiprocessing import shared_memory, managers

class Server():
    def __init__(self, dataloader, size, name='server_share_data', address=('127.0.0.1', 5566), authkey=b'server_torch_manager'):
        SyncManager = managers.SyncManager
        SyncManager.register('next', self.next)
        self.manager = SyncManager(address=address, authkey=authkey)
        self.name = name
        self.pid = os.getpid()
        self.address = address
        self.authkey = authkey

        shared_data = {
            'pid': self.pid,
            'address': self.address,
            'authkey': self.authkey,
        }
        shared_data_pkl = pickle.dumps(shared_data)

        self.shm_shared_data = shared_memory.SharedMemory(self.name, create=True, size=len(shared_data_pkl))
        self.shm_shared_data.buf[:] = shared_data_pkl[:]

        self.dataloader = dataloader
        self.size = size
        self.shm_data = shared_memory.SharedMemory(name='server_torch_data', create=True, size=size)
        self.iterloader = iter(self.dataloader)

        self.manager.get_server().serve_forever()

    def next(self):
        try:
            data = next(self.iterloader)
        except StopIteration:
            self.iterloader = iter(self.dataloader)
            data = next(self.iterloader)
        data_pkl = pickle.dumps(data)
        data_len = len(data_pkl)
        self.shm_data.buf[:data_len] = data_pkl
