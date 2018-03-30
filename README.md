# Intro to Machine Learning

Codes and notes from Udacity [Intro to Machine Learning](https://eu.udacity.com/course/intro-to-machine-learning--ud120) course.

## Requirements

In order to run the sample codes, you'll need the following packages:

* [Python 2.7](https://www.python.org)
* [NumPy](http://www.numpy.org)
* [SciPy](https://www.scipy.org)
* [matplotlib](https://matplotlib.org)
* [scikit-learn](http://scikit-learn.org)
* [nltk](https://www.nltk.org)

## Installation

If you don't have Python installed, heads up to the [Python Download Page](https://www.python.org/downloads/). All the codes are tested using Python version 2.7.

Run the following command to install all of the required dependencies:

```shell
$ pip install -U numpy scipy matplotlib scikit-learn nltk
```

This project is also use the Enron dataset. To download the dataset run the following commands:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# RUn the startup script.
$ python tools/startup.py
```

The startup script will also check for all of the required modules. The Enron dataset is around 400 MB, so it may take a while to complete. You should get the similar output on your terminal:

```shell
✅ nltk is installed.
✅ numpy is installed.
✅ scipy is installed.
✅ sklearn is installed.
✅ matplotlib is installed.
⏳ Downloading the Enron dataset, this may take a while...
✅ Enron dataset is downloaded: /path/to/intro-to-machine-learning/data/enron_mail_20150507.tar.gz
⏳ Unzipping Enron dataset, this may take a while...
✅ Enron dataset is extracted to: /path/to/intro-to-machine-learning/data
🎉 You're ready to go!
```

## Chapters

* [Naive Bayes](https://github.com/risan/intro-to-machine-learning/tree/master/naive_bayes#readme)
* [Support Vector Machine](https://github.com/risan/intro-to-machine-learning/tree/master/svm#readme)

## New Things I Learned

* [Python Notes](https://github.com/risan/intro-to-machine-learning/tree/master/python-notes.md)
* [Scikit and SciPy Notes](https://github.com/risan/intro-to-machine-learning/tree/master/scikit-and-scipy-notes.md)
