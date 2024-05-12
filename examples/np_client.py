import time
from datamana.numpy import Client

client = Client('numpy')
loop = 200
start_time = time.time()

for _ in range(loop):
    data = client.next()
    print(data.shape)
    time.sleep(0.1)

end_time = time.time()
print(f'avg time: {(end_time - start_time) / loop}')
