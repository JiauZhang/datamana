import time, os
from datamana.ipc import Semaphore

sem = Semaphore('datamana-01')
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
