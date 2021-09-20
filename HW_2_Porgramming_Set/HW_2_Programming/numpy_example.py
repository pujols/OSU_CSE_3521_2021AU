import argparse
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define numpy arrays
A = np.random.rand(3, 5)
B = np.zeros((3, 1))
C = np.ones((1, 3))
D = np.linspace(0, 5, num=6)

# Print
print(A)
print(B)
print(C)
print(D)

# Print shapes
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)

print(A.ndim)
print(B.ndim)
print(C.ndim)
print(D.ndim)

# Reshape
print(D.reshape(6, 1)) # 6-by-1 matrix (column vector)
print(D.reshape(6, 1).shape)
print(D.reshape(6, 1).ndim)

print(D.reshape(1, 6)) # 1-by-6 matrix (row vector)
print(D.reshape(1, 6).shape)
print(D.reshape(1, 6).ndim)

print(D.reshape(-1, 1))
print(D.reshape(-1, 1).shape)
print(D.reshape(-1, 1).ndim)


# Extract element (note that, numpy index starts from 0)
print(A)
print(A[1,1])
print(A[:, 1])
print(A[1, :])
print(A[1, -1])
print(A[1, 0:3])

# matrix transpose
print(A)
print(A.transpose())

# real values
print(-4)
print((-4)**0.5)
print(np.real(-4**0.5))

# matrix multiplication
print(np.matmul(A.transpose(), A))
print(np.matmul(A, A.transpose()))
print(np.matmul(B, C))
print(np.matmul(C, B))

# matrix inversion
print(np.linalg.inv(np.matmul(A, A.transpose())))

# eigendecomposition
Sigma = np.matmul(A, A.transpose())
V, W = np.linalg.eig(Sigma)
print(V)
print(np.argsort(V))
print(np.argsort(V)[::-1])
print(V[np.argsort(V)])