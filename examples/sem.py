import time, os
from datamana.core import Semaphore

sem = Semaphore()
errno = sem.open('datamana-01', os.O_CREAT, 666, 1)
if errno != 0:
    print(f'Semaphore open failed! <{os.strerror(errno)}>')
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
