# GaussianNB Deployment on Terrain Data

Use scikit-learn [Gaussian Naive Bayes](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) classifier to classify terrain data and plot the decision boundary.

## Table of Contents

* [Modules Breakdown](#modules-breakdown)
    * [Generate Random Terrain Data](#generate-random-terrain-data)
    * [The Gaussian Naive Bayes Classifier](#the-gaussian-naive-bayes-classifier)
    * [Plot the Decision Boundary](#plot-the-decision-boundary)
* [Python Tips and Tricks](#python-tips-and-tricks)
    * [Generate an Array of Random Numbers](#generate-an-array-of-random-numbers)
    * [Pair Values from Two Array](#pair-values-from-two-array)
    * [Splitting an Array](#splitting-an-array)
    * [Multiple Returns in Python](#multiple-returns-in-python)
    * [Create and Train Gaussian Naive Bayes Classifier](#create-and-train-gaussian-naive-bayes-classifier)
    * [Numpy Create Range of Values with The Given Interval](#numpy-create-range-of-values-with-the-given-interval)
    * [Numpy Create Coordinate Matrices from Coordinate Vectors](#Numpy-create-coordinate-matrices-from-coordinate-vectors)
    * [Flatten Numpy Array](#flatten-numpy-array)
    * [Pairing Array Values with Second Axis](#pairing-array-values-with-second-axis)
    * [Generate Coordinates Across The Grid](#generate-coordinates-across-the-grid)
    * [Plot The Surface Decision](#plot-the-surface-decision)
    * [Filtering Array In One Line](#filtering-array-in-one-line)
    * [Scatter Plot](#scatter-plot)

## Modules Breakdown

### Generate Random Terrain Data

The `terrain_data_generator.py` is used to generate a random terrain data. It accepts the optional `total_points` parameter, which determines the total number of points that needs to be generated (default to `1000`).

```py
from terrain_data_generator import generateTerrainData

features_train, labels_train, features_test, labels_test = generateTerrainData([total_points=1000])
```

### The Gaussian Naive Bayes Classifier

The `nb_classifier.py` is used to create and train the classifier. It uses the scikit-learn [Gaussian Naive Bayes](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) classifier. Pass the training features and labels to the `trainClassifier` function, it will then return the classifier instance.

```py
from nb_classifier import trainClassifier

classifier = trainClassifier(features_train, labels_train)
```

## Plot the Decision Boundary

The `plot.py` is used to plot both the test points and the predicted decision boundary.

```py
from plot import predictAndPlot

predictAndPlot(classifier, features_test, labels_test)
```

![Decision Boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/02_naive_bayes/19_gaussian_nb_deployment_on_terrain_data/scatter_plot.png)

## Python Tips and Tricks

### Generate an Array of Random Numbers

Use the `for..in` syntax to generate an array of random numbers in one line.

```py
import random

# Initialize internal state of random generator.
random.seed(42)

# Generate random points.
randomNumbers = [random.random() for i in range(0, 10)]
# [0.6394267984578837, 0.025010755222666936, 0.27502931836911926, ...]
```

### Pair Values from Two Array

The built-in `zip` function can pair values from two array, but it will return an array of tuples. To get an array of pairs, we can combine it with `for..in`:

```py
coordinates = [[x, y] for x,y in zip([5,10,15], [0,1,0])]
# [[5, 0], [10, 1], [15, 0]]
```

### Splitting an Array

We can easily split an array in Python by specifying the starting index and it's ending index. The ending index is excluded. You can specify a negative index. And both of these indices are optional.

```py
a = [0,1,2,3,4,5]

a[0:3]  # 0,1,2
a[1:3]  # 1,2
a[2:]   # 2,3,4,5
a[:3]   # 0,1,2
a[0:-2] # 0,1,2,3
a[-2:]  # 4,5
a[:]    # 0,1,2,3,4,5
```

### Multiple Returns in Python

In Python you can return multiple values seperated by commas.

```py
def test():
    return 100, "foo"

someNumber, someString = test()
```

### Create and Train Gaussian Naive Bayes Classifier

With scikit-learn we can easily create and train a Gaussian Naive Bayes classifier:

```py
from sklearn.naive_bayes import GaussianNB

# Create the classifier instance.
classifier = GaussianNB()

# Train the classifier.
classifier.fit(features_train, labels_train)

# Predict the output labels.
clasifier.predict(features_test)
```

### Numpy Create Range of Values with The Given Interval

With Numpy, we can easily create an array within the specified range with evenly spaced interval:

```py
import numpy as np

np.arange(0, 5, 1)
# array([0,1,2,3,4])

np.arange(1, 4, 0.5)
# array([1. , 1.5, 2. , 2.5, 3. , 3.5])
```

### Numpy Create Coordinate Matrices from Coordinate Vectors

We can use Numpy `meshgrid` function to make coordinate matrices from one-dimentional coordinate arrays.

```py
import numpy as np

np.meshgrid([1, 2, 3], [0, 7])
# [
#   array([[1,2,3], [1,2,3]]),
#   array([[0,0,0], [7,7,7]])
# ]
```

### Flatten Numpy Array

When we have a multi-dimensional Numpy array, we caneasily flatten it with `ravel` method:

```py
import numpy as np

arr = np.array([[1,2], [3,4]])
arr.ravel()
# array([1, 2, 3, 4])
```

### Pairing Array Values with Second Axis

We can use Numpy `c_` function to pair array values with another array that will be it's second axis.

```py
import numpy as np

x = [1,2]
y = [10,20]

np.c_[x, y]
# array([1,10], [2,20])
```

### Generate Coordinates Across The Grid

With the knowledge of Numpy `arange`, `meshgrid`, `ravel` and `c_` function, we can easily generate coordinates across the grid so we can pass it to the clasifier and plot the decision surface.

```py
import numpy as np

# Generate an evenly spaced coordinates.
x_points, y_points = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

# Pair the x and y points.
test_coordinates = np.c_[x_points.ravel(), y_points.ravel()]
```

### Plot The Surface Decision

We can pass the coordinates across the grid to the clasifier to predict the output on each coordinate. We can then use `matplotlib` to plot the surface decision.

```py
import matplotlib.pyplot as plt
import pylab as pl

# Pass coordinates across the grid.
predicted_labels = classifier.predict(test_coordinates)

# Don't forget to reshape the output array dimension.
predicted_labels = predicted_labels.reshape(x_points.shape)

# Set the axes limit.
plt.xlim(x_points.min(), x_points.max())
plt.ylim(y_points.min(), y_points.max())

# Plot the decision boundary with seismic color map.
plt.pcolormesh(x_points, y_points, predicted_labels, cmap = pl.cm.seismic)
```

The classifier output would be 1 dimensional array, so don't forget to `reshape` it back into two dimensional array before plotting. The `cmap` is optional parameter for the color map. Here we use the `seismic` color map from `pylab` module. It has the red-blue colors.

### Filtering Array In One Line

We can easily filter an array by combinning the `for..in` and `if` syntaxs together.

```py
numbers = range(1,11)

# Filter even numbers only.
[numbers[i] for i in range(0, len(numbers)) if numbers[i] % 2 == 0]
# [2, 4, 6, 8, 10]
```

### Scatter Plot

we need to seperate the test points based on its predicted label (the speed). So we can plot the test points with two different colors.

```py
# Separate fast (label = 0) & slow (label = 1) test points.
grade_fast = [features_test[i][0] for i in range(0, len(features_test)) if labels_test[i] == 0]
bumpy_fast = [features_test[i][1] for i in range(0, len(features_test)) if labels_test[i] == 0]
grade_slow = [features_test[i][0] for i in range(0, len(features_test)) if labels_test[i] == 1]
bumpy_slow = [features_test[i][1] for i in range(0, len(features_test)) if labels_test[i] == 1]

# Plot the test points based on its speed.
plt.scatter(grade_fast, bumpy_fast, color = "b", label = "fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label = "slow")

# Show the plot legend.
plt.legend()

# Add the axis labels.
plt.xlabel("grade")
plt.ylabel("bumpiness")

# Show the plot.
plt.show()
```

If you want to save the plot into an image, you can use the `savefig` method instead:

```py
plt.savefig('scatter_plot.png')
```
