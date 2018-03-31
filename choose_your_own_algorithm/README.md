# Choose Your Own Algorithm

We're going to use three different algorithms here:

* K-Nearest Neighbors: classic, simple, easy to understand
* Random Forest
* AdaBoost

Both Random Forest and AdaBoost are belong to the "ensemble methods"—it's a meta classifier built usually from multiple decision trees.

## Table of Contents

* [K-Nearest Neighbors](#k-nearest-neighbors)
    * [K-Nearest Neighbors Strengths and Weaknesses](#k-nearest-neighbors-strengths-and-weaknesses)
* [Random Forest](#random-forest)
    * [Random Forest Strengths and Weaknesses](#random-forest-strengths-and-weaknesses)
* [AdaBoost](#adaboost)
    * [AdaBoost Strengths and Weaknesses](#adaboost-strengths-and-weaknesses)
* [K-Nearest Neighbors](#k-nearest-neighbors)
    * [K-Nearest Neighbors Strengths and Weaknesses](#k-nearest-neighbors-strengths-and-weaknesses)
* [Random Forest](#random-forest)
* [Terrain Classifier](#terrain-classifier)
    * [Terrain Classifier with K-Nearest Neighbors](#terrain-classifier-with-k-nearest-neighbors)
    * [Terrain Classifier with Random Forest](#terrain-classifier-with-random-forest)
    * [Terrain Classifier with AdaBoost](#terrain-classifier-with-adaboost)

## K-Nearest Neighbors

* In K-Nearest Neighbors a point is classified by the majority of class on its surounding neighbors.
* Let's say that the `k = 3`, that means an unknown object will be classified based on its `3` nearest neighbors.

To illustrate how this K-Nearest Neighbors works, check the following image from [Wikipedia](https://en.wikipedia.org/wiki/File:KnnClassification.svg).

![KNN Illustration](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/slides/knn-illustration.png)

Suppose we would like to classify the green-circle point at the center. There are two possible classes: the red-triangle and the blue-square.

* If the `k = 3` (solid line circle), the green-circle will be classified as the red-triangle as there are more red-triangles inside this solid line circle.
* If the `k = 5` (dotted line circle), the green-circle will be classified as the blue-square as there are four blue-squares compared to the only two red-triangles here.

### K-Nearest Neighbors Strengths and Weaknesses

* Robust to noisy training data.
* Effective when training data is large.
* At the same time it also computationally expensive when dealing with a large dataset.

## Random Forest

* Random Forest is an ensemble method that use multiple decision trees.
* Unlike decision tree, in Random Forest the process of finding the root node and splitting the features run randomly.
* Random Forest overcome the Decision Tree's issue that prones to overfitting. As long as there are enough trees in the forest, it won't overfit the model.
* Random Forest works by creating multiple Decision Tree classifiers with random set of features. It then predict the data by running it through these multiple classifiers and choose the most voted output.

Random Forest diagram by [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2015/06/tuning-random-forest-model/).

![Random Forest Diagram](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/slides/random-forest-diagram.png)

### Random Forest Strengths and Weaknesses

* For classification problem, the Random Forest can avoid overfitting issue.
* Beside for for solving classification problem, it can also be used for regression task.
* It can be used to identify the most important features from training dataset.
* It computationally more expensive compared to the Decision Tree.

## AdaBoost

* AdaBoost or Adaptive Boosting is also an ensemble method that built upon multiple "week learners".
* This "week learner" can be any types of learning algorithms but it usually using the Decision Tree.
* AdaBoost will train this week learner iteratively by choosing the training set based on the accuracy of the previous training.
* It then weight each trained classifier at any iteration based on its accuracy.
* Although on each iteration AdaBoost choose a random subset of training data, it still gives more weight to the previously missclasified data points so these points have more probability to be included in the current iteration.

Checkout the AdaBoost illustration by [Grey Atom](https://medium.com/greyatom/a-quick-guide-to-boosting-in-ml-acf7c1585cb5) below:

![Random Forest Diagram](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/slides/adaboost-illustration.png)

1. First it draws a decision boundary at D1, where other 3 pluses are missclasified.
2. The 3 pluses that are missclasified on the previous iteration are given more weight now, thus the decision boundary is moved to D2. Now there are three minuses on the lest that are missclasified.
3. The 3 minuses that are missclasified are now given more weight causing the decision boundary move to D3.
4. Finally we combine the D1, D2, D3 to form a strong classifier.

### AdaBoost Strengths and Weaknesses

* It can be used with may types of learning algorithms.
* It can be sensitive to noisy data and outlier.
* It can overcome the overfitting issue.

## Terrain Classifier

### Terrain Classifier with K-Nearest Neighbors

With sklearn we can easily create the [K-Nearest Neighbors classifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html):

```py
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier()
```

Type the following command on your terminal to run the terrain classifier with K-Nearest Neighbors:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python choose_your_own_algorithm/terrain_classifier/k_nearest_neighbors
```

The result from using the K-Nearest Neighbors classifier to predict the vehicle's speed given a terrain condition.

```txt
# n_neighbors = 5 (default)
# weight = uniform (default)
🤖 Accuracy: 0.92
```

![K-Nearest Neighbors decision boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/k_nearest_neighbors/plot.png)

We can pass the `n_neighbors` parameter to specify the number of neighbors to use. Here's the better result with `n_neighbors = 10`:

```txt
# n_neighbors = 10
# weight = uniform (default)
🤖 Accuracy: 0.932
```

![K-Nearest Neighbors n_neighbors10](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/k_nearest_neighbors/n_neighbors_10.png)

There's also the `weight` parameter to specify the function to weight points on neighborhood. The default is `uniform` which means all points on each neighbor are weight equally. There's also `distance` option which mean points on closer neighborhood have more influence compared to the one that far away.

```txt
# n_neighbors = 5 (default)
# weight = distance
🤖 Accuracy: 0.932
```

![K-Nearest Neighbors n_neighbors10](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/k_nearest_neighbors/weight_distance.png)

Tweaking both the `n_neighbors` and the `weight` parameters give use the best result:

```txt
# n_neighbors = 10
# weight = distance
🤖 Accuracy: 0.94
```

![K-Nearest Neighbors n_neighbors10](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/k_nearest_neighbors/n_neighbors10_weight_distance.png)

### Terrain Classifier with Random Forest

To create the [Random Forest classifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) with sklearn:

```py
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier()
```

Type the following command on your terminal to run the terrain classifier with Random Forest:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python choose_your_own_algorithm/terrain_classifier/random_forest
```

The result from using the Random Forest classifier to predict the vehicle's speed given a terrain condition.

```txt
# n_estimators = 10 (default)
# criterion = gini (default)
🤖 Accuracy: 0.92
```

![Random Forest decision boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/random_forest/plot.png)

There's `criterion` parameter that we can pass to specify the function that will measure the quality of the split. By default it's using the Gini impurity (`gini`). If we want to use the infomation gain instead, pass the `entropy`. It turns out using the `entropy` decrease our accuracy:

```
# n_estimators = 10 (default)
# criterion = entropy
🤖 Accuracy: 0.908
```

![Random Forest creterion entropy](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/random_forest/criterion_entropy.png)

We can pass the `n_estimators` to specify the number of trees in the forest. The default value is `10` and by increasing it by a little bit, we got slightly better accuracy:

```txt
# n_estimators = 15
# criterion = gini (default)
🤖 Accuracy: 0.924
```

![Random Forest n_estimators 15](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/random_forest/n_estimators_15.png)

### Terrain Classifier with AdaBoost

To create the [AdaBoost classifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html) with sklearn:

```py
from sklearn.ensemble import AdaBoostClassifier

classifier = AdaBoostClassifier()
```

Type the following command on your terminal to run the terrain classifier with AdaBoost:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python choose_your_own_algorithm/terrain_classifier/adaboost
```

The result from using the AdaBoost classifier to predict the vehicle's speed given a terrain condition.

```txt
🤖 Accuracy: 0.924
```

![Adaboost decision boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/choose_your_own_algorithm/terrain_classifier/adaboost/plot.png)
