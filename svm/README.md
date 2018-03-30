# Support Vector Machine

## Table of Contents

* [SVM Summary](#svm-summary)
* [Terrain Classifier with SVM](#terrain-classifier-with-svm)
    * [Create and Train a Gaussian SVM Classifier](#create-and-train-a-gaussian-svm-classifier)
    * [Run the Classifier](#run-the-classifier)
    * [Terrain Classifier Result](#terrain-classifier-result)

## SVM Summary

* SVM is a supervised learning model.
* It takes an input of data with two categories and create a line that separate these two categories.
* It find the maximum distance or margin between the line and the nearest point from both of the categories.
* It puts the correctness of the classification first before trying to maximize the margin.

## Terrain Classifier with Naive Bayes

### Create and Train a SVM Classifier

We can use the [SVM classifier](http://scikit-learn.org/stable/modules/svm.html) easily with scikit-learn:

```py
from sklearn import svm

# Create and train the classifier.
classifier = svm.SVC(kernel = "linear")
classifier.fit(features_train, labels_train)

# Predict the output labels.
clasifier.predict(features_test)
```

### Run the Classifier

Type the following command on your terminal to run the terrain classifier:

```shell
# Go to the terrain_classifier directory.
$ cd /path/to/svm/terrain_classifier

# And run it with Python
$ python terrain_classifier.py
```

### Terrain Classifier Result

The result from using the SVM classifier to predict the vehicle's speed given a terrain condition.

```txt
🤖 Accuracy: 0.92
```

![Gaussian Naive Bayes decision boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/plot.png)
