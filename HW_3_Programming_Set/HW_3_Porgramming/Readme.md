# Homework 3

## Submission instructions

* Due date and time: November 12 (Friday), 11:59 pm ET

* Carmen submission: 
Submit one .zip file named HW3_programming_name_number.zip (e.g., HW3_programming_chao_209.zip), which contains the following files
  - your completed python script `NaiveBayes.py`
  - your improved python script `NaiveBayes_improved.py` (see **Naive Bayes Classification: improvement (10 pts)** below)
  - a short report (no more than one page), saved as a pdf named `name.number.pdf` (see **What to submit** at the end)
  - a `collaboration.txt` which lists with whom you have discussed the homework (see more details below).
 
* Collaboration: You may discuss the homework with your classmates. However, you need to write your own solutions and submit them separately. In your submission, you need to list with whom you have discussed the homework in a .txt file collaboration.txt. Please list each classmate’s name and name.number (e.g., Wei-Lun Chao, chao.209) as a row in the .txt file. That is, if you discussed with two classmates, your .txt file will have two rows. If you did not discuss with your classmates, just write "no discussion" in collaboration.txt. Please consult the syllabus for what is and is not an acceptable collaboration.

## Implementation instructions

* Download or clone this repository.

* You will see the directory named `NaiveBayes`, the file `collaboration.txt`, and a PPT `HW_3_How_To.pptx`.

* The slide [HW_3_How_To.pptx](./HW_3_How_To.pptx) privdes some further instruction about this assignment.
 
* You will see a [`data-sentiment`](`NaiveBayes/data-sentiment/`) folder inside the  [`NaiveBayes/`](./NaiveBayes/) directory, which contains the training data (`train/Positive.txt`, `train/Neutral.txt`, `train/Negative.txt`) and the test data (`test/Positive.txt`, `test/Neutral.txt`, `test/Negative.txt`).

* Please use python3 and write your own solutions from scratch. You may need NumPy.

* **Caution! python and NumPy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.**

* If you use Windows, we recommend that you run the code in the Windows command line. You may use `py -3` instead of `python3` to run the code.

* Caution! Please do not import packages (like scikit learn or nltk) that are not listed in the provided code. Follow the instructions in each question strictly to code up your solutions. Do not change the output format. Do not modify the code unless we instruct you to do so. (You are free to play with the code but your submitted code should not contain those changes that we do not ask you to do.) A homework solution that does not match the provided setup, such as format, name, initializations, etc., will not be graded. It is your responsibility to make sure that your code runs with the provided commands and scripts.



# Introduction

In this homework, you are to implement the Naive Bayes algorithm for tweet classifications for sentiment analysis. You will play with the Twitter Senitment Analysis data, where each tweet sentence is tagged/labeled as with either Positive, Negative, or Neutral sentiment.


# Data Description

The directory structure of the [data](./NaiveBayes/data-sentiment/) folder is given below:

```
./NaiveBayes/data-sentiment/
		├── train
		│   ├── Negative.txt
		│   ├── Neutral.txt
		│   └── Positive.txt
		└── test
		    ├── Negative.txt
		    ├── Neutral.txt
		    └── Positive.txt
```

* The [train](./NaiveBayes/data-sentiment/train/) sub-folder contains the data for training your Naive Bayes model. 
	* There are 3098 total sentences in the train data. 
	* [Negative.txt](./NaiveBayes/data-sentiment/train/Negative.txt) file cotnains 893 tweets with Negative Sentiment
	* [Neutral.txt](./NaiveBayes/data-sentiment/train/Neutral.txt) file cotnains 1256 tweets with Neutral Sentiment
	* [Positive.txt](./NaiveBayes/data-sentiment/train/Positive.txt) file cotnains 949 tweets with Positive Sentiment


* The [test](./NaiveBayes/data-sentiment/test/) sub-folder contains the data that you will used to test the performance of your Naive Bayes model. 
	* There are 775 total sentences in the test data. 
	* [Negative.txt](./NaiveBayes/data-sentiment/test/Negative.txt) file cotnains 224 tweets with Negative Sentiment
	* [Neutral.txt](./NaiveBayes/data-sentiment/test/Neutral.txt) file cotnains 314 tweets with Neutral Sentiment
	* [Positive.txt](./NaiveBayes/data-sentiment/test/Positive.txt) file cotnains 237 tweets with Positive Sentiment


# Naive Bayes Classification (50 pts)

* You will implement Naive Bayes in this question. You are to amend your implementation into [`NaiveBayes.py`](./NaiveBayes/NaiveBayes.py). You have to first represent each sentence by a binary bag of word (BoW) vector. That is, a vector records if a unique word (e.g., "good") shows up in a sentence. See the `HW_3_How_To.pptx` slides for more details.

* There are many sub-functions in [`NaiveBayes.py`](./NaiveBayes/NaiveBayes.py). You can ignore all of them except the following two:
	* [`def train(self, training_sentences, training_labels):`](./NaiveBayes/NaiveBayes.py#L94)
		* You need to estimate the parameter of the probabiltiy of each class label and save them in `self.prior`. You may use any data structure (e.g., list, NumPy array).

		* You need to estimate the parameter of the conditional probabiltiy of each unique word given a class `c` and save them in `self.conditional`. You may use any data structure (e.g., list, NumPy array). For example, you can create a NumPy array `self.conditional`, where `self.conditional[i][j]` records the conditional probability of seeing the "j-th" unique word in the dictionary in sentences of the "i-th" class.

		* Debugging Tips: print the variable `self.prior` and check if it is storing the the expected probablity values for that class.

	* [`def predict(self, test_sentence):`](./NaiveBayes/NaiveBayes.py#L119). 
		* You have to find the **log** probability (see details in the `HW_3_How_To.pptx` slides) for each class label for each given `test_sentence` and store them in the `label_probability` variable. Remember we have 3 labels in this dataset: Positive(+1), Negative(-1), Neutral (0).
		
		* Debugging Tips: print the variable [`label_probability`](./NaiveBayes/NaiveBayes.py#L138) and check if it is returning the expected values.

* **You may create a function in [`class NaiveBayesClassifier(object):`](./NaiveBayes/NaiveBayes.py#L60) to build the binary BoW representation for each sentence.**

* Detailed instruction: [HW_3_How_To.pptx](./HW_3_How_To.pptx)
  

## Auto grader:

* You may run the following command to test your implementation<br/>
`python3 NaiveBayes.py`<br/>

* You might see a warning like `RuntimeWarning: divide by zero encountered in log`. No worries for now. Your code will proceed to output the results.

* You should achieve an accuracy around 74%. 

* Note that, the auto grader is to check your implementation semantics. If you have syntax errors, you may get python error messages before you can see the auto_graders' results.

* Again, the auto_grader is just to simply check your implementation. It may not be used for your final grading.


# Naive Bayes Classification: improvement (10 pts)

As mentioned above, you may see `RuntimeWarning: divide by zero encountered in log`.

* Now, can you think of a way to resolve this warning, and accordingly get an even higher accuracy?

* Hint: think about what causes the warning, and what this warning means for a test sentence. We talked about pseduo count in the class in estimating the parameters. Do you think it will help resolve the problem?

* TODO: 
	* Make a copy of your completed `python3 NaiveBayes.py`, and name the copy as `NaiveBayes_improved.py`.
	* Implement your solution for `RuntimeWarning: divide by zero encountered in log` in `NaiveBayes_improved.py`. Note that, changing the python output option to block the warning is not a solution here.
	* Write in `name.number.pdf` a short paragraph of what your solution is.
	
* After implementation, you may run the following command to test your implementation<br/>
`python3 NaiveBayes_improved.py`<br/>

You should see exactly the same output format as `python3 NaiveBayes.py`, but the resulting accuracy may improve.


# What to submit:

* Your completed python script `NaiveBayes.py`. 
* Your improved python script `NaiveBayes_improved.py`.
* Your report `name.number.pdf`. The report should contain the following four answers: 
	* **(1)** the output from `python3 NaiveBayes.py` (i.e., accuracy; how many are correct),
	* **(2)** the output from `python3 NaiveBayes_improved.py` (i.e., accuracy; how many are correct), 
	* **(3)** a short paragraph of what you did in `python3 NaiveBayes_improved.py`, 
* a `collaboration.txt` which lists with whom you have discussed the homework.
* Please follow **Submission instructions** to submit a .zip file HW3_programming_name_number.zip (e.g., HW3_programming_chao_209.zip), which contains the above four files.
