from multiprocessing import Process, shared_memory
import signal, os, time
from threading import Thread

name = 'shm'
size = 32
shm = shared_memory.SharedMemory(name=name, create=True, size=size)
print(shm.name, shm.size)
# shm.close()
time.sleep(60)
