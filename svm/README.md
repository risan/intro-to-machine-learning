# Support Vector Machine

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

## SVM Summary

* SVM is a supervised learning model.
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
