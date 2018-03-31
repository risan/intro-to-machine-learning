# Support Vector Machine

Support Vector Machine or SVM is one of the supervised learning model.

## Table of Contents

* [SVM Summary](#svm-summary)
* [Terrain Classifier with SVM](#terrain-classifier-with-svm)
    * [Create and Train a Gaussian SVM Classifier](#create-and-train-a-gaussian-svm-classifier)
    * [Run the Classifier](#run-the-classifier)
    * [Terrain Classifier Result](#terrain-classifier-result)
* [SVM Parameters](#svm-parameters)
    * [The C Parameter](#the-c-parameter)
    * [The Gamma Parameter](#the-gamma-parameter)
    * [Playing with SVM Parameters](#playing-with-svm-parameters)
* [SVM Strengths and Weaknesses](#svm-strengths-and-weaknesses)
* [Email Classifier with SVM](#email-classifier-with-svm)
    * [Speeding Up the SVM](#speeding-up-the-svm)
    * [Using RBF Kernel with Various C Parameter](#using-rbf-kernel-with-various-c-parameter)

## SVM Summary

* It takes an input of data with two categories and create a line that separate these two categories.
* It find the maximum distance or margin between the line and the nearest point from both of the categories.
* It puts the correctness of the classification first before trying to maximize the margin.
* SVM can solve not only the linearly separated classes, but the non-linear classes too.
* SVM tackle the non-linearly separated classes by using the kernel trick. It transform the low dimensional inputs into a higher dimensional inputs that are linearly separarable.
* Sklearn provided several built-in kernel that we can use with SVM SVC: `linear`, `poly`, `rbf` (default value), `sigmoid`, `precomputed`.

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
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python svm/terrain_classifier
```

### Terrain Classifier Result

The result from using the SVM classifier to predict the vehicle's speed given a terrain condition.

```txt
🤖 Accuracy: 0.92
```

![SVM decision boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/plot.png)

## SVM Parameters

You can configure various parameters when working with SVM SVC module from scikit-learn. Some of them are:

* `kernel`: The kernel type to use. There are several built-in kernel that we can use: `linear`, `poly`, `rbf` (default value), `sigmoid`, `precomputed`. We can also provide our custom kernel function.
* `gamma`: Is the kernel coefficient for `rbf`, `poly` and `sigmoid` (default to `auto`, `1/n_features`).
* `C`: Penalty parameter of the error term (default to `1.0`).

> ⚠️ Beware of overfitting! Overfitting is when your algorithm take data point too literally, resulting in a complex decision boundary. If not careful, these three parameters may lead you to overfitting. Tuning these parameters is an art of the machine learning.

### The C Parameter

The `C` parameter is a trade-off between the smoothness of the decision boundary and the correctness of the classifier. The larger the value, the more correct points it will be, but the boundary line might not smooth and straight.

### The Gamma Parameter

The `gamma` parameter defines how far is the influence of a single training data.

Low value means each point has the far reach. Thus when calculating the decision boundary, even the data point that are far away from the boundary get considered. On this case, the decision boundary would be more smooth.

The high value means each point has only the close reach. Thus when calculating the decision boundary, data points that are close to the boundary has more influences compared to the one that far away. On this case, the decision boundary tends to be more jagged.

### Playing with SVM Parameters

```txt
kernel: linear
C: 1.0 (default)

🤖 Accuracy: 0.92
```

![SVM Linear Kernel](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/linear.png)

```txt
kernel: rbf
C: 1.0 (default)
gamma: auto (default)

🤖 Accuracy: 0.92
```

![SVM RBF Kernel](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/rbf.png)

```txt
kernel: rbf
C: 1000
gamma: auto (default)

🤖 Accuracy: 0.924
```

![SVM RBF Kernel C1000](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/rbf_c1000.png)

```txt
kernel: rbf
C: 1.0 (auto)
gamma: 1000

🤖 Accuracy: 0.924
```

![SVM RBF Kernel Gamma1000](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/rbf_gamma1000.png)

```txt
kernel: rbf
C: 1000
gamma: 1000

🤖 Accuracy: 0.912
```

![SVM RBF Kernel C1000 Gamma1000](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/svm/terrain_classifier/rbf_c1000_gamma1000.png)

## SVM Strengths and Weaknesses

* It works really well on a complex domain where there are clear margin of separation.
* It doesn't work really well when dealing with a large dataset. The training time complexity is quadratic with the number of samples making it hard to scale dealing with more than a couple of 10,000 samples.
* It doesn't work well with high noise data, where many points from different classes are overlapping each other (Better to use Naive Bayes on this case).

## Email Classifier with SVM

Type the following command on your terminal to run the email classifier:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python svm/email_classifier
```

The result of using SVM classifier with linear kernel to predict the email's author:

```txt
⏱ Training time: 178.436s
⏱ Predicting time: 17.618s
🤖 Accuracy: 0.9840728100113766
```

### Speeding Up the SVM

With the same email dataset, compared to Gaussian Naive Bayes, SVM took longer to train and predict. To make the process faster, we can cut down the number of testing data.

```txt
# The result with only 1% of training data.
⏱ Training time: 0.091s
⏱ Predicting time: 0.996s
🤖 Accuracy: 0.8845278725824801
```

Compared to the previous test, we now only use 1% of testing data. Both the training and predicting times are speeding-up significanly. Yet the accuracy is only drop 0.1, not bad right? The speed of predicting can be essential in a system for detecting credit card fraud or voice recognition like Siri.

### Using RBF Kernel with Various C Parameter

Still with 1% of training data, here are the results of using RBF kernel and various `C` parameter:

```txt
# C = 1.0 (default)
⏱ Training time: 0.104s
⏱ Predicting time: 1.153s
🤖 Accuracy: 0.6160409556313993

# C = 10.0
⏱ Training time: 0.108s
⏱ Predicting time: 1.158s
🤖 Accuracy: 0.6160409556313993

# C = 100.0
⏱ Training time: 0.104s
⏱ Predicting time: 1.277s
🤖 Accuracy: 0.6160409556313993

# C = 1000.0
⏱ Training time: 0.116s
⏱ Predicting time: 1.115s
🤖 Accuracy: 0.8213879408418657

# C = 10000.0
⏱ Training time: 0.096s
⏱ Predicting time: 0.899s
🤖 Accuracy: 0.8924914675767918
```

The biggest `C` has the best accuracy, the bigger `C` also means more complex decision boundary. Now with all of the training data incuded:

```txt
# C = 10000.0
⏱ Training time: 119.813s
⏱ Predicting time: 13.032s
🤖 Accuracy: 0.9908987485779295

👦 Total emails from Chris: 877
👧 Total emails from Sarah: 881
```

We have 99% of accuracy! It's amazing, but as you may see both the training and predicting process took times. Working with text document like this, we'd better off using Naive Bayes.
