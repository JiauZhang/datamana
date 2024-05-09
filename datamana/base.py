from datamana.ipc import Semaphore, MQueue, SharedMemory
import numpy as np

class Base():
    def __init__(self, name):
        self.data_name = f'datamana{name}'
        self.data_meta_name = f'{self.data_name}meta'
        self.data_share_name = f'{self.data_name}share'
        self.data_sem_name = f'{self.data_name}sem'
        self.data_mq_tx_name =f'{self.data_name}mqtx'
        self.data_mq_rx_name =f'{self.data_name}mqrx'
        self.sem = Semaphore(self.data_sem_name)
        self.mq_tx = MQueue(self.data_mq_tx_name)
        self.mq_rx = MQueue(self.data_mq_rx_name)
        self.name2shm = {}

    def get_shm(self, shm_name, size, **kwargs):
        if shm_name in self.name2shm:
            shm = self.name2shm[shm_name]
            if size > 0: shm.resize(size)
        else:
            shm = SharedMemory(name=shm_name, size=size, **kwargs)
            self.name2shm[shm_name] = shm
        return shm

    def write_byte(self, shm, data, size):
        shm.resize(size)
        shm.buf[:size] = data[:]

    def write_numpy(self, shm, data):
        np_shm = np.ndarray(data.shape, dtype=data.dtype, buffer=shm.buf)
        np_shm[:] = data[:]

    def server_send(self, msg, msg_prio=0):
        return self.mq_tx.send(msg, msg_prio)

    def server_recv(self):
        return self.mq_rx.receive()

    def client_send(self, msg, msg_prio=0):
        return self.mq_rx.send(msg, msg_prio)

    def client_recv(self):
        return self.mq_tx.receive()
