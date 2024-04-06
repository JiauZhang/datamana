import torch
from datamana.torch import Server

fake_tensors = [
    torch.randn(32, 3, 512, 512) for _ in range(4)
]

server = Server(fake_tensors)
