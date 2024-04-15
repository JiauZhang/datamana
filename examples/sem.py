import time, os
from datamana.core import Semaphore, fcntl

sem = Semaphore()
if sem.open('datamana-01', fcntl.O_CREAT, 666, 1) == -1:
    print('sem open failed!')
    exit(-1)
count = 0
pid = os.getpid()

while count < 20:
    sem.wait()
    print(f'pid[{pid}] got sem!')
    time.sleep(0.5)
    print(f'pid[{pid}] post sem...')
    sem.post()
    count += 1
    time.sleep(0.5)

sem.close()
