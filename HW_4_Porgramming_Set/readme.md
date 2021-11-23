# Homework-4: Logistic Regression and Perceptron

## Submission instructions

* Due date and time: December 8 (Wednesday), 23:59 ET

* Carmen submission: 
Submit a .zip file named `HW4_programming_name_number.zip` (e.g., HW4_programming_chao_209.zip), which contains
  - your completed python script `Linear_Classifiers.py`
  - A short report (no more than one page), saved as a pdf named `HW4_programming_name_number.pdf` (see **What to submit** at the end)
  - a `collaboration.txt` which lists with whom you have discussed the homework (see more details below). 
 
* Collaboration: You may discuss the homework with your classmates. However, you need to write your own solutions and submit them separately. In your submission, you need to list with whom you have discussed the homework in a .txt file `collaboration.txt`. Please list each classmate’s name and name.number (e.g., Wei-Lun Chao, chao.209) as a row in the .txt file. That is, if you discussed with two classmates, your .txt file will have two rows. If you did not discuss with your classmates, just write "no discussion" in `collaboration.txt`. Please consult the syllabus for what is and is not an acceptable collaboration.


## Implementation instructions

* Download or clone this repository.

* You will see a python file name `Linear_Classifiers.py`

* You will see a PPT file named `HW-4.pptx`

* Download the data `Starplus.npz` from Carmen (which is under `Files/Homework 4`) and put it in the same folder as `Linear_Classifiers.py`

* Please use python3 and write your own solutions from scratch. You may need NumPy.

* **Caution! python and NumPy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.**

* We note that, the provided commands are designed to work with Mac/Linux with Python version 3. If you use Windows (like me!), we recommend that you run the code in the Windows command line (CMD). You may use `py -3` instead of `python3` to run the code. You may use editors like PyCharm to write your code.

* Caution! Please do not import packages (like scikit learn or nltk) that are not listed in the provided code. Follow the instructions in each question strictly to code up your solutions. Do not change the output format. Do not modify the code unless we instruct you to do so. (You are free to play with the code but your submitted code should not contain those changes that we do not ask you to do.) A homework solution that does not match the provided setup, such as format, name, initializations, etc., will not be graded. It is your responsibility to make sure that your code runs with the provided commands and scripts.


# Introduction

In this homework, you are to implement logistic regression and perceptron algorithms for binary linear classification.

We have provided slides for implementation details in [`HW-4.pptx`](./HW-4.pptx)


## Data: 

* The binary classification is about whether a human subject is viewing a picture or reading a sentence, using their fMRI brain image data as input. The data comes from the [starplus dataset](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-81/www/) (only the first subject). 

* We have converted the matlab format data into Python/Numpy arrays (i.e., `Starplus.npz`). 

* Each data instance is a brain image that we have flattened into a feature vector `X[:, n]` (both `X_train` or `X_test` are in this format already). That is, a data instance is a column vector. Your task is to train a classifier that outputs the predicted label. The values of predicted/true label `y` are: `{+1,-1}`, which correspond to whether the subject was shown a picture or a sentence.

* **NOTE-1:** It may take some time to run the experiments for this assignment, so we recommend that you start early. 

* **NOTE-2:** We have also created a simple 2-dimensional data set for developing your code.

* **NOTE-3:** We have concatenate "1" to the end of each data instance. Thus, the linear classifier can be represented as `sign(w^T * x)`, where `^T` means transpose and `w` has included `b` in its last element.



# Logistic Regression (30 points)

Recall the logistic regression algorithm that we have discussed in class. Your task will be to implement logistic regression with gradient descent by completing the following sections in `Linear_Classifiers.py`. 

## Implementation

* You are to implement the gradient descent updating rule in `def Logisitc_Regression`.

* There are many sub-functions in  [`Linear_Classifiers.py`](./Linear_Classifiers.py). You can ignore all of them except the following two:
	* [`def Logisitc_Regression(X, Y, learningRate=0.01, maxIter=100):`](./Linear_Classifiers.py#L90)
    		
		* Your implementation should go to [`####### TODO: implement logistic regression`](./Linear_Classifiers.py#L107). **Your implementation should be fewer than 15 lines.**
	
	* [`def sigmoid(a):`](./Linear_Classifiers.py#L86)
    		
		* This is the element-wise sigmoid function that you may find useful. The function takes a value, a vector, or a matrix as input and performs the sigmoid fuction to each element independently. 

* After your implementation, you can first run the following command on the simple 2-dimensional data for a fast check:

```
python3 Linear_Classifiers.py --data simple --algorithm logistic

```
You will see your accuracy around
  * Accuracy: training set: around 1.0
  * Accuracy: training set: around 1.0


* You can further run the following command on the starplus data:

```
python3 Linear_Classifiers.py --data starplus --algorithm logistic

```
You will see your accuracy around
  * Accuracy: training set: around 1.0
  * Accuracy: training set: around 0.71



# Perceptron (30 points)

Recall the perceptron algorithm that we have discussed in class. Your task will be to implement perceptron by completing the following sections in `Linear_Classifiers.py`. 

## Implementation

* You are to implement the updating rule in `def Perceptron`.

* There are many sub-functions in  [`Linear_Classifiers.py`](./Linear_Classifiers.py). You can ignore all of them except the following one:
	* [def Perceptron(X, Y, learningRate=0.01, maxIter=100):](./Linear_Classifiers.py#L116)
	* Your implementation should go to [`####### TODO: implement perceptron`](./Linear_Classifiers.py#L138). **Your implementation should be fewer than 15 lines.**

* After your implementation, you can first run the following command on the simple 2-dimensional data for a fast check:

```
python3 Linear_Classifiers.py --data simple --algorithm perceptron

```
You will see your accuracy around
  * Accuracy: training set: around 1.0
  * Accuracy: training set: around 1.0


* You can further run the following command on the starplus data

```
python3 Linear_Classifiers.py --data starplus --algorithm perceptron

```
You will see your accuracy around
  * Accuracy: training set: around 1.0
  * Accuracy: training set: around 0.78



# What to submit:

* Your completed python script `Linear_Classifiers.py`. 
* Your report `HW4_programming_name_number.pdf`. The report should contain the following four answers: 
	* **(1)** the output from `python3 Linear_Classifiers.py --data simple --algorithm logistic` (i.e., training and test accuracy),
	* **(2)** the output from `python3 Linear_Classifiers.py --data starplus --algorithm logistic` (i.e., training and test accuracy),
	* **(3)** the output from `python3 Linear_Classifiers.py --data simple --algorithm perceptron` (i.e., training and test accuracy),
	* **(4)** the output from `python3 Linear_Classifiers.py --data starplus --algorithm perceptron` (i.e., training and test accuracy),
* A `collaboration.txt` which lists with whom you have discussed the homework. 
* Please follow **Submission instructions** to submit a .zip file named HW4_programming_name_number.zip (e.g., HW4_programming_chao_209.zip), which contains the above three files.
