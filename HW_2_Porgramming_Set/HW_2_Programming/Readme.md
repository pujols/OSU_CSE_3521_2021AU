# Homework 2

## Submission instructions

* Due date and time: October 12st (Tuesday), 11:59 pm ET

* Expected time commitment: 10 hrs

* Carmen submission: 
Submit one .zip file named HW2_programming_name_number.zip (e.g., HW2_programming_chao_209.zip), which contains
  - your completed python script `DR.py` (for dimensionality reduction - Question 1)
  - your completed python script `LR.py` (for linear regression - Question 2)
  - your 6 generated results for Question 1: `MNIST_2.png`, `Swiss_Roll_2.png`, `toy_data_2.png`, `Results_MNIST_2.npz`, `Results_Swiss_Roll_2.npz`, and `Results_toy_data_2.npz`.
  - your 4 generated results for Question 2: `linear_1.png`, `quadratic_2.png`, `Results_linear_1.npz`, and `Results_quadratic_2.npz`
  - a `collaboration.txt` which lists with whom you have discussed the homework (see more details below). 

* Collaboration: You may discuss the homework with your classmates. However, you need to write your own solutions and submit them separately. In your submission, you need to list with whom you have discussed the homework in a .txt file `collaboration.txt`. Please list each classmate’s name and name.number (e.g., Wei-Lun Chao, chao.209) as a row in the .txt file. That is, if you discussed with two classmates, your .txt file will have two rows. If you did not discuss with your classmates, just write "no discussion" in `collaboration.txt`. Please consult the syllabus for what is and is not an acceptable collaboration.

## Implementation instructions

* Download or clone this repository.

* You will see four python scripts: `DR.py`, `LR.py`, `feature_normalization.py`, and `numpy_example.py`. You will also see `collaboration.txt`.

* You will see a `data` folder, which contains `mnist_test.csv`, `Linear.npz`, `Quadratic.npz`, and `Swiss_Roll.npz`.

* You will see a folder `for_display`, which simply contains some images used for display here.

* Please use python3 and write your own solutions from scratch. 

* **Caution! python and NumPy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.**

* If you use Windows, we recommend that you run the code in the Windows command line. You may use `py -3` instead of `python3` to run the code.

* Caution! Please do not import packages (like scikit learn) that are not listed in the provided code. Follow the instructions in each question strictly to code up your solutions. Do not change the output format. Do not modify the code unless we instruct you to do so. (You are free to play with the code but your submitted code should not contain those changes that we do not ask you to do.) A homework solution that does not match the provided setup, such as format, name, initializations, etc., will not be graded. It is your responsibility to make sure that your code runs with the provided commands and scripts.

## Installation instructions

* You will be using [NumPy] (https://numpy.org/), and your code will display your results with [matplotlib] (https://matplotlib.org/). If your computer does not have them, you may install with the following commands:
  - for NumPy: <br/>
    do `sudo apt install python3-pip` or `pip3 install numpy`. If your are using Windows command line, you may try `setx PATH "%PATH%;C:\Python34\Scripts"`, followed by `py -3 -mpip install numpy`.

  - for matplotlib: <br/>
    do `python3 -m pip install -U pip` and then `python3 -m pip install -U matplotlib`. If you are using the Windows command line, you may try `py -3 -mpip install -U pip` and then `py -3 -mpip install -U matplotlib`.



# Introduction

In this homework, you are to implement principal component analysis (PCA) for dimensionality reduction and linear regression and apply your completed algorithms to multiple different datasets to see their pros and cons.

* In Question 1, you will play with Swiss Roll data, MNIST (digit data), and some other toy datasets.

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/Swiss.png)

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/Digits.png)


* In Question 2, you will play with simple linear and quadratic data (x-axis is the feature variable; y-axis is the real-value label; each point is a data instance: red for training and blue for testing) and some other toy datasets.

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/linear_1.png)

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/quadratic_2.png)


# Question 0: Exercise

* You will use [NumPy] (https://numpy.org/) extensively in this homework. NumPy a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. NumPy has many great functions and operations that will make your implementation much easier. 

* If you are not familiar with Numpy, we recommend that you read this [tutorial] (https://cs231n.github.io/python-numpy-tutorial/) or some other tutorials online, and then play with some code to get familiar with it.

* We have provided some useful Numpy operations that you may want to use in `numpy_example.py`. You may want to comment out all the lines first, and execute them one by one or in a group to see the results and the differences. You can run the command `python3 numpy_example.py`.

* We also provide another python script `feature_normalization.py`, which will guide you through L2 normalization, covariance matrices, z-score, and whitening. You may find some code here helpful for your implementation. You can run the command `python3 feature_normalization.py`.

* In `DR.py` and `LR.py`, we also provide some more instructions and hints for what functions or operations you may want to use.

* Caution! python and NumPy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.


# Question 1: Dimensionality reduction (50 pts)

* You will implement PCA in this question. You are to amend your implementation into `DR.py`.

* There are many sub-functions in `DR.py`. You can ignore all of them but `def PCA(X, out_dim)` and `main(args)`. In `main(args)`, you will see a general pipeline of machine learning: <br/>
  - Loading data: `X, phi = data_loader(args)`, in which `X` is a D-by-N matrix (numpy array) and each column is a data instance. You can type `X[:, 0]` to extract the "first" data instance from `X`. (**Caution! python and numpy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.**) To ensure that `X[:, 0]` is a column vector, you may do `X[:, 0].reshape(-1, 1)`, which will give you a column vector of size D-by-1. <br/>
  - Learning patterns: `mu, W = PCA(np.copy(X), out_dim)`, in which the code takes `X` and the desired output dimensions as input and output the mean vector `mu` and the projection matrix (numpy array) `W`.
  - Apply the learned patterns to the data: which will be part of your job to implement.
  
## Coding:

You have two parts to implement in `DR.py`:

* The function `def PCA(X, out_dim)`: please go to the function and read the input format, output format, and the instructions (for what to do) carefully. You can assume that the actual inputs will follow the input format, and your goal is to generate the required numpy arrays (`mu` and `Sigma`), which will be used to compute the outputs. Please make sure that your results follow the required numpy array shapes. You are to implement your code between `### Your job 1 starts here ###` and `### Your job 1 ends here ###`. You are free to create more space between those two lines: we include them just to explicitly tell you where you are going to implement.

* Apply the learned patterns: After obtaining the mean vector `mu` and the projection matrix (numpy array) `W`, you are to apply them to your data `X`. You are to implement your code between `### Your job 2 starts here ###` and `### Your job 2 ends here ###`. Again, you are free to create more space between those two lines. You can assume that `X`, `mu`, and `W` are already defined, and your goal is to create the matrix (numpy array) `new_X`, which is out_dim-by-N (out_dim and N are both already defined). Each column (data instance) of `new_X` corresponds to the same column in `X`.

## Auto grader:

* You may run the following command to test your implementation<br/>
`python3 DR.py --data simple_data --auto_grade`<br/>
Note that, the auto grader is to check your implementation semantics. If you have syntax errors, you may get python error messages before you can see the auto_graders' results.

* Again, the auto_grader is just to simply check your implementation for a toy case. It will not be used for your final grading.

## Play with different datasets (Task 1 - toy data):

* Please run the following command<br/>
`python3 DR.py --data toy_data --method PCA --out_dim 2 --display --save`<br/>
This command will run PCA on a simple angle shape data in 3D and project it to 2D (defined by --out_dim 2). You will see the resulting mean vector and projection matrix being displayed in your command line. You will also see a figure showing the data before and after PCA. Points of similar colors mean that they are similar, and PCA does preserve such similarity.

* The code will generate `toy_data_2.png` and `Results_toy_data_2.npz`, which you will include in your submission.

* You may play with other commands by (1) removing `--save` (2) changing the `--out_dim 2` to 1. You may also remove `--display` if you don't want to display the figure.


## Play with different datasets (Task 2 - MNIST):

* Please run the following command<br/>
`python3 DR.py --data MNIST --method PCA --out_dim 2 --display --save`<br/>
This command will run PCA on 1010 digit images of digit "3". The size of each image is 28-by-28, or equivalently a 784-dimensional vector. We are to perform PCA to reduce its dimensionality (e.g., to 2) and then use the two dimensions to reconstruct the 28-by-28 image. You will see a figure showing multiple images. The leftmost image is the mean image. The second to the right and the rightmost images are one original "3" image and the reconstructed image. The middle images show you the projections (here there are two projections). Note that, in doing PCA, we vectorize an image and get a mean vector and a projection matrix with several principal components. Then to display them, we then reshape them back to images.

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/MNIST.png)

* The code will generate `MNIST_2.png` and `Results_MNIST_2.npz`, which you will include in your submission.

* You may play with other commands by (1) removing `--save` (2) changing the `--out_dim 2` to some other non-negative integers (e.g., 1, 3, 4, 200). You will see that the reconstructed images get closer to the original image when out_dim approaches 784. 

## Play with different datasets (Task 3 - Swiss Roll):

* Please run the following command<br/>
`python3 DR.py --data Swiss_Roll --method PCA --out_dim 2 --display --save`<br/>
This command will run PCA on the 3D Swiss Roll dataset to reduce the dimensionality to 2D. You will see the resulting mean vector and projection matrix being displayed in your command line. You will also see a figure showing the data before and after PCA. Points of similar colors mean that they are similar (following the Swiss Roll shape in and out). You will see that PCA cannot preserve the similarity. This is because that PCA can only do linear projection: simply flatten the roll but not unfold it.

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/Swiss_Roll.png)

* The code will generate `Swiss_Roll_2.png` and `Results_Swiss_Roll_2.npz`, which you will include in your submission.

* You may play with other commands by (1) removing `--save` (2) changing the `--out_dim 2` to 1. You may also remove `--display` if you don't want to display the figure.

## What to submit:

* Your completed python script `DR.py`

* Your 6 generated results for Question 1: `MNIST_2.png`, `Swiss_Roll_2.png`, `toy_data_2.png`, `Results_MNIST_2.npz`, `Results_Swiss_Roll_2.npz`, and `Results_toy_data_2.npz`.

## Extension: nonlinear dimensionality reduction (No worries! We have implemented it for you!)

Above you see that PCA cannot preserve the similarity (neighbors) along with the Swiss Roll. Remember that in the lecture we introduce nonlinear dimensionality reduction algorithms that aim to preserve the neighbors. Here you are to play with one algorithm, Laplacian Eigenmap (LE).

* Please run the following command<br/>
`python3 DR.py --data Swiss_Roll --method LE --out_dim 2 --display`<br/>
This command will run LE on the 3D Swiss Roll dataset to reduce the dimensionality to 2D. You will also see a figure showing the data before and after LE. Points of similar colors mean that they are similar (following the Swiss Roll shape in and out). You will see that LE can preserve the similarity, unfolding the roll.

![Alt text](https://github.com/pujols/OSU_CSE_3521_2021AU/blob/master/HW_2_Porgramming_Set/HW_2_Programming/for_display/Swiss_LE.png)

* You do not need to submit anything for this extension.



# Question 2: Linear regression (50 pts)
* You will implement linear regression in this question. You are to amend your implementation into `LR.py`.

* There are many sub-functions in `LR.py`. You can ignore all of them but `def linear_regression(X, Y)` and `def main(args)`. In `main(args)`, you will see a general pipeline of machine learning: <br/>
  - Loading data: `X_original, Y = data_loader(args)`, in which `X` is a 1-by-N matrix (numpy array) and each column is a data instance. You can type `X[:, 0]` to extract the "first" data instance from `X`. (Caution! python and numpy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.) <br/>
  - Feature transform: `X = polynomial_transform(np.copy(X_original), args.polynomial)` extends each column of `X` to its polynomial representation. For example, given x, this transform will extends it to [x, x^2, ..., x^(args.polynomial)]^T.
  - Learning patterns: `w, b = linear_regression(X, Y)`, in which the code takes `X` and the desired labels `Y` as input and output the weights `w` and the bias `b`.
  - Apply the learned patterns to the data: `training_error = np.mean((np.matmul(w.transpose(), X) + b - Y.transpose()) ** 2)` and `test_error = np.mean((np.matmul(w.transpose(), X_test) + b - Y_test.transpose()) ** 2)` compute the training and test error.
  
## Coding:

You have one part to implement in `LR.py`:

* The function `def linear_regression(X, Y)`: please go to the function and read the input format, output format, and the instructions carefully. You can assume that the actual inputs will follow the input format, and your goal is to generate the required numpy arrays (`w` and `b`), the weights and bias of linear regression. Please make sure that your results follow the required numpy array shapes. You are to implement your code between `### Your job starts here ###` and `### Your job ends here ###`. You are free to create more space between those two lines: we include them just to explicitly tell you where you are going to implement.

## Auto grader:

* You may run the following command to test your implementation<br/>
`python3 LR.py --data simple --auto_grade`<br/>
Note that, the auto grader is to check your implementation semantics. If you have syntax errors, you may get python error messages before you can see the auto_graders' results.

* Again, the auto_grader is just to simply check your implementation for a toy case. It will not be used for your final grading.

## Play with different datasets (Task 1 - linear data):

* Please run the following command<br/>
`python3 LR.py --data linear --polynomial 1 --display --save`<br/>
This command will run linear regression on a 1D linear data (the x-axis is the feature and the y-axis is the label). You will see the resulting `w` and `b` being displayed in your command line. You will also see the training (on red points) and test error (on blue points). 

* The code will generate `linear_1.png` and `Results_linear_1.npz`, which you will include in your submission.

* You may play with other commands by (1) removing `--save` (2) changing the `--polynomial 1` to a non-negative integer (e.g, 2, 3, ..., 15). You will see that, while larger values lead to smaller training errors, the test error is not necessarily lower. For very large value, the test error can go very large.


## Play with different datasets (Task 2 - quadratic data):

* Please run the following command<br/>
`python3 LR.py --data quadratic --polynomial 2 --display --save`<br/>
This command will run linear regression on a 1D quadratic data (the x-axis is the feature and the y-axis is the label). The code will produce polynomial = 2 representation for the data (i.e., `X` becomes 2-by-N). You will see the resulting `w` and `b` being displayed in your command line. You will also see the training (on red points) and test error (on blue points). 

* The code will generate `quadratic_2.png` and `Results_quadratic_2.npz`, which you will include in your submission.

* You may play with other commands by (1) removing `--save` (2) changing the `--polynomial 2` to a non-negative integer (e.g, 1, 3, ..., 15). You will see that, while larger values lead to smaller training error, the test error is not neccessarily lower. For very large value, the test error can go verly large.

## What to submit:

* Your completed python script `LR.py`

* Your 4 generated results for Question 2: `linear_1.png`, `quadratic_2.png`, `Results_linear_1.npz`, and `Results_quadratic_2.npz`
