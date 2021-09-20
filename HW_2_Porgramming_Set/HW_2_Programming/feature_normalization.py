import argparse
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# This is a code to go through the idea of feature normalization

## Data creation: I create a 2-by-10 matrix, where each data point/instance is 2-dimensional, and I have 10 instances
X = np.zeros((2, 10))
phi = np.random.rand(10)
noise = np.random.rand(10)
X[0, :] = 3 * phi
X[1, :] = phi + 0.3 * noise
D = X.shape[0] # 2
N = X.shape[1] # 10



## Plot the original data
fig, ax = plt.subplots()
ax.scatter(X[0, :], X[1, :], color='black')
plt.title('Original data')
plt.show()
plt.close(fig)



## Compute the L2 norm and perform normalization
print("################################### Now in L2 normalization", "\n")
norm_X = np.sum(X ** 2, 0) ** 0.5 # the "0" dimension is row-wise
norm_X = norm_X.reshape(1, -1)
print("L2 norm of each data instance: ", norm_X)
print("\n")

normalized_X = X / norm_X # each column of X divided by each element of norm_X
# print("L2 normalized data instances: ", normalized_X)
#print("\n")
## Plot the original data
fig, ax = plt.subplots()
ax.scatter(normalized_X[0, :], normalized_X[1, :], color='black')
plt.title('L2-normalized data')
plt.show()
plt.close(fig)

norm_normalized_X = np.sum(normalized_X ** 2, 0) ** 0.5
norm_normalized_X = norm_normalized_X.reshape(1, -1)
print("L2 norm of each data instance after L2 normalization: ", norm_normalized_X)
print("\n")



## Compute the mean
print("################################### Now in the mean", "\n")
mu = np.mean(X, 1).reshape(-1, 1) # the "1" dimension is column-wise
print("mu: ", mu)
print("\n")

fig, ax = plt.subplots()
ax.scatter(X[0, :], X[1, :], color='black')
ax.scatter(mu[0], mu[1], color='red') # show the mean location as the red point
plt.title('Original data and its mean')
plt.show()
plt.close(fig)

bar_X = X - mu # each column subtracted by mu
print("mu of bar_X: ", np.mean(bar_X, 1).reshape(-1, 1))
print("mu bar_X is almost 0, with some numerical error")
print("\n")



## Compute the covariance matrix (three ways)
print("################################### Now in the covariance matrix", "\n")
Sigma_1 = np.zeros((D, D)) # 2-by-2 covariance
for i in range(D):
    for j in range(D):
        for n in range(N):
            Sigma_1[i, j] += (X[i, n] - mu[i]) * (X[j, n] - mu[j])
Sigma_1 = Sigma_1 / N
print("Covariance matrix is: ", Sigma_1)
print("\n")

Sigma_2 = np.zeros((D, D)) # 2-by-2 covariance
for n in range(N):
    x_n = X[:, n].reshape(-1,1)
    Sigma_2 += np.matmul((x_n - mu), (x_n - mu).transpose())
Sigma_2 = Sigma_2 / N
print("Covariance matrix is: ", Sigma_2)
print("\n")

Sigma_3 = np.matmul(bar_X, bar_X.transpose())
Sigma_3 = Sigma_3 / N
print("Covariance matrix is: ", Sigma_3)
print("\n")

print("Do you see that these three ways of computations lead to the same covariance matrix?")
print("\n")



## Z-score
print("################################### Now in Z-score", "\n")
std_X = np.std(X, axis = 1, keepdims = True)
print("Standard deviation of X: ", std_X)
print("\n")

Z = (X - mu) / std_X
std_Z = np.std(Z, axis = 1, keepdims = True)
mu_Z = np.mean(Z, 1).reshape(-1, 1)
print("mu of Z: ", mu_Z)
print("mu of Z is almost 0, with some numerical error")
print("\n")
print("Standard deviation of Z: ", std_Z)
print("Standard deviation of Z is 1")
print("\n")

fig, ax = plt.subplots()
ax.scatter(Z[0, :], Z[1, :], color='black')
plt.title('Z-score data')
plt.show()
plt.close(fig)


## Whitening
print("################################### Now in whitening", "\n")
Sigma_inv = np.linalg.inv(Sigma_3)
Lambda, Q = np.linalg.eigh(Sigma_inv)
Lambda = np.diag(Lambda ** 0.5)
Sigma_inv_05 = np.matmul(Lambda, Q.transpose())
Z = np.matmul(Sigma_inv_05, X - mu)
print("mu of Z: ", np.mean(Z, 1).reshape(-1, 1))
print("mu of Z is almost 0, with some numerical error")
print("\n")
print("Standard deviation of Z: ", np.std(Z, axis = 1, keepdims = True))
print("Standard deviation of Z is 1")
print("\n")
Sigma_Z = np.matmul(Z, Z.transpose()) / N
print("Covariance matrix of Z: ", Sigma_Z)
print("Covariance matrix of Z is an identity matrix")
print("\n")

fig, ax = plt.subplots()
ax.scatter(Z[0, :], Z[1, :], color='black')
plt.title('Whitened data')
plt.show()
plt.close(fig)


