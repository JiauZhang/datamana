from datamana.torch import Client

client = Client()

for _ in range(200):
    data = client.next()
    print(data.shape)
