from datamana.numpy import Client

client = Client('numpy')

for _ in range(200):
    data = client.next()
    print(data.shape)
