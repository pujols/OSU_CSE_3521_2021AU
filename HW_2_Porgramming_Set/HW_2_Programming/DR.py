import argparse
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


## Data loader and data generation functions
def data_loader(args):
    """
    Output:
        X: the data matrix (numpy array) of size D-by-N
        phi: a numpy array of size N that records the color or label of each data instance
    """
    if args.data == "Swiss_Roll":
        print("Using Swiss_Roll")
        X, phi = data_swiss_roll()
    elif args.data == "toy_data":
        print("Using toy_data")
        X, phi = toy_data()
    elif args.data == "MNIST":
        print("Using MNIST")
        X, phi = data_MNIST(args)
    else:
        print("Using simple_data")
        X, phi = simple_data()
    return X, phi


def data_swiss_roll():
    """
    length_phi = 15  # length of swiss roll in angular direction
    length_Z = 5  # length of swiss roll in z direction
    sigma = 0.1  # noise strength
    m = 1000  # number of samples
    X = np.zeros((3, m))
    phi = length_phi * np.random.rand(m)
    xi = np.random.rand(m)
    X[0] = 1. / 6 * (phi + sigma * xi) * np.sin(phi)
    X[1] = 1. / 6 * (phi + sigma * xi) * np.cos(phi)
    X[2] = length_Z * np.random.rand(m)
    np.savez('Swiss_Roll.npz', X = X, phi = phi)
    """
    data = np.load(osp.join(args.path, 'Swiss_Roll.npz'))
    X = data['X']
    phi = data['phi']
    return X, phi


def data_MNIST(args):
    X = np.loadtxt(osp.join(args.path, "mnist_test.csv"), delimiter=",")
    X = X.astype('float64')
    Y = X[:, 0]
    X = X[Y == 3, 1:].transpose()
    return X, np.ones(X.shape[1])


def toy_data():
    m = 100
    m = 2 * int(m/2)
    X = np.zeros((3, m))
    X[0] = np.linspace(-8.0, 10.0, num=m)
    X[1] = np.linspace(-1.0, 3.0, num=m)
    X[2] = np.concatenate((np.linspace(1.0, 2.0, num=int(m/2)), np.linspace(2.0, 1.0, num=int(m/2))), 0)
    return X, X[0]


def simple_data():
    m = 5
    X = np.zeros((2, m))
    X[0] = np.linspace(0.0, 10.0, num=m)
    X[1] = np.linspace(0.0, 3.0, num=m)
    return X, X[0]


## Displaying the results
def display_DR(args, new_X, X, phi, mu, W):
    if args.data == "Swiss_Roll" or args.data == "toy_data":
        if new_X.shape[0] != 1:
            fig = plt.figure()
            ax = fig.add_subplot(211, projection='3d')
            ax.scatter(X[0], X[1], X[2], c=phi, cmap=plt.cm.Spectral)
            ax.set_title("Original data")
            ax = fig.add_subplot(212, projection='3d')
            ax.scatter(new_X[0], new_X[1], c=phi, cmap=plt.cm.Spectral)
            plt.title('Projected data')
            plt.axis('tight')
            plt.xticks([]), plt.yticks([])
            if args.method == "PCA" and args.save:
                plt.savefig(args.data + '_' + str(args.out_dim) + '.png', format='png')
                np.savez('Results_' + args.data + '_' + str(args.out_dim) + '.npz', mu = mu, W = W)
            plt.show()
            plt.close(fig)
        else:
            print("The output dimensionality has to be larger than 1 for a scatter plot!")
    elif args.data == "MNIST":
        if args.method == "PCA":
            xx = X[:, 0].reshape(-1, 1)
            new_xx = new_X[:, 0].reshape(-1, 1)
            new_xx = np.matmul(W, new_xx) + mu
            to_show = np.concatenate((mu, W[:, :min(5, args.out_dim)], xx, new_xx), 1)
            fig, axes = plt.subplots(1, min(5, args.out_dim) + 1 + 1 + 1, figsize=(28, 28),
                                     subplot_kw={'xticks': [], 'yticks': []},
                                     gridspec_kw=dict(hspace=0.1, wspace=0.1))
            for i, ax in enumerate(axes.flat):
                ax.imshow(to_show[:, i].reshape(28, 28), cmap='bone')
            print("The first image is the mean image. the second to the last and the last are an"
                  " original digit image and its reconstruction. Images in the middle are PCA components"
                  " (columns of W, after reshaped).")
            if args.method == "PCA" and args.save:
                plt.savefig(args.data + '_' + str(args.out_dim) + '.png', format='png')
                np.savez('Results_' + args.data + '_' + str(args.out_dim) + '.npz', mu=mu, W=W)
            plt.show()
            plt.close(fig)
        else:
            print("No display for LE on MNIST!")
    else:
        print("new_X is: ", new_X)
        if args.method == "PCA" and args.save:
            np.savez('Results_' + args.data + '_' + str(args.out_dim) + '.npz', mu=mu, W=W)


## auto_grader
def auto_grade(mu, W):
    print("In auto grader!")
    if mu.ndim != 2:
        print("Wrong dimensionality of mu")
    else:
        if mu.shape[0] != 2 or mu.shape[1] != 1:
            print("Wrong shape of mu")
        else:
            if sum((mu - [[5.], [1.5]]) ** 2) < 10 ** -6:
                print("Correct mu")
            else:
                print("Incorrect mu")

    if W.ndim != 2:
        print("Wrong dimensionality of W")
    else:
        if W.shape[0] != 2 or W.shape[1] != 1:
            print("Wrong shape of W")
        else:
            if  1.01 > np.matmul(W.transpose(), np.array([[0.95782629], [0.28734789]])) > 0.99 or \
                -0.99 > np.matmul(W.transpose(), np.array([[0.95782629], [0.28734789]])) > -1.01:
                print("Correct W")
            else:
                print("Incorrect W")


## Dimensionality reduction functions
def LE(X, out_dim, num_neighbor=5):
    """
    Input:
        X: a D-by-N matrix (numpy array) of the input data
        out_dim: the desired output dimension
        num_neighbors: the number of neighbors to be preserved
    Output:
        new_X: the out_dim-by- N data matrix (numpy array) after dimensionality reduction
    """

    X = np.copy(X)
    D = X.shape[0]  # dimensionality of X
    N = X.shape[1]  # number of data instances of X

    # Build the pairwise distance matrix
    Dis = np.matmul(X.transpose(), X)
    Dis = np.matmul(Dis.diagonal().reshape(-1, 1), np.ones((1, N))) + \
          np.matmul(np.ones((N, 1)), Dis.diagonal().reshape(1, -1)) - \
          2 * Dis
    Dis_order = np.argsort(Dis, 1)

    # Build the similarity matrix. We set the num_neighbor neighbors of each data instance to 1; others, 0.
    Sim = np.zeros((N, N))
    for n in range(N):
        Sim[n, Dis_order[n][1:1+num_neighbor]] = 1
    Sim = np.maximum(Sim, Sim.transpose())
    DD = np.diag(np.sum(Sim, 1))
    L = DD - Sim # Laplacian matrix

    V, W = np.linalg.eig(np.matmul(np.linalg.inv(DD), L))
    V = V.real
    W = W.real
    V_order = np.argsort(V)
    V = V[V_order]
    W = W[:, V_order]
    new_X = W[:, 1:1+out_dim].transpose()

    return new_X


def PCA(X, out_dim):
    """
    Input:
        X: a D-by-N matrix (numpy array) of the input data
        out_dim: the desired output dimension
    Output:
        mu: the mean vector of X. Please represent it as a D-by-1 matrix (numpy array).
        W: the projection matrix of PCA. Please represent it as a D-by-out_dim matrix (numpy array).
            The m-th column should correspond to the m-th largest eigenvalue of the covariance matrix.
            Each column of W must have a unit L2 norm.
    Todo:
        1. build mu
        2. build the covariance matrix Sigma: a D-by-D matrix (numpy array).
        3. We have provided code of how to compute W from Sigma
    Useful tool:
        1. np.mean: find the mean vector
        2. np.matmul: for matrix-matrix multiplication
        3. the builtin "reshape" and "transpose()" function of a numpy array
    """

    X = np.copy(X)
    D = X.shape[0] # feature dimension
    N = X.shape[1] # number of data instances

    ### Your job 1 starts here ###
    mu = ...
    Sigma = ...

    ### Your job 1 ends here ###

    """
        np.linalg.eigh (or np.linalg.eig) for eigendecomposition.
        V: eigenvalues, W: eigenvectors
        This function has already L2 normalized each eigenvector.
    """
    V, W = np.linalg.eigh(Sigma)
    V = V.real  # the output may be complex value: do .real to keep the real part
    W = W.real  # the output may be complex value: do .real to keep the real part
    V_order = np.argsort(V)[::-1]  # sort the eigenvalues in the descending order
    V = V[V_order]
    W = W[:, V_order] # sort in the descending order
    W = W[:, :out_dim] # output the top out_dim eigenvectors
    return mu, W


## Main function
def main(args):

    if args.auto_grade:
        args.data = "simple_data"
        args.method = "PCA"
        args.out_dim = int(1)
        args.display = False
        args.save = False

    ## Loading data
    X, phi = data_loader(args) # X: the D-by-N data matrix (numpy array); phi: metadata of X (you can ignore it)

    ## Setup
    out_dim = int(args.out_dim) # output dimensionality
    D = X.shape[0]  # dimensionality of X
    N = X.shape[1]  # number of data instances of X
    print("Data size: ", X.shape)

    # Running DR
    # Running PCA
    if args.method == "PCA":
        print("Method is PCA")
        mu, W = PCA(np.copy(X), out_dim) # return mean and the projection matrix (numpy array)
        if args.data != "MNIST":
            print("The mean vector is: ", mu)
            print("The projection matrix is: ", W)

        ### Your job 2 starts here ###
        """
        Create a out_dim-by-N matrix (numpy array) named "new_X" to store the data after PCA.
        In other words, you are to apply mu and W to X
        1. new_X has size out_dim-by-N
        2. each column of new_X corresponds to each column of X
        3. Useful tool: check the "np.matmul" function and the builtin "transpose()" function of a numpy array 
        4. Hint: Just one line of code
        """
        new_X = ...

        ### Your job 2 ends here ###

    elif args.method == "LE":
        print("Method is LE")
        new_X = LE(np.copy(X), out_dim)
        mu = 0
        W = 0

    else:
        print("Wrong method!")

    # Display the results
    if args.display:
        display_DR(args, new_X, X, phi, mu, W)

    if args.auto_grade:
        auto_grade(mu, W)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Running dimensionality reduction (DR)")
    parser.add_argument('--path', default="data", type=str)
    parser.add_argument('--data', default="Swiss_Roll", type=str)
    parser.add_argument('--method', default="PCA", type=str)
    parser.add_argument('--out_dim', default=2, type=int)
    parser.add_argument('--display', action='store_true', default=False)
    parser.add_argument('--save', action='store_true', default=False)
    parser.add_argument('--auto_grade', action='store_true', default=False)
    args = parser.parse_args()
    main(args)
