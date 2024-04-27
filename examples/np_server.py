import numpy as np
from datamana.numpy import Server

fake_tensors = [
    np.random.randn(32, 3, 256, 256),
    np.random.randn(32, 3, 256, 512),
    np.random.randn(32, 3, 512, 512),
    np.random.randn(32, 3, 512, 256),
]

server = Server('numpy', fake_tensors)
server.serve()
