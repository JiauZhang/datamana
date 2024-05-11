import torch
from datamana.torch import Server

fake_tensors = [
    torch.randn(32, 3, 256, 256),
    torch.randn(32, 3, 256, 512),
    torch.randn(32, 3, 512, 512),
    torch.randn(32, 3, 512, 256),
]

server = Server('torch', fake_tensors)
server.serve()
