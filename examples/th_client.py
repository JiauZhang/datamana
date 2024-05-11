from datamana.numpy import Client

client = Client('torch')

for _ in range(200):
    data = client.next()
    print(data.shape, data.device)
