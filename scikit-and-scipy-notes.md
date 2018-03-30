# SciPy and Scikit Learn Stuff

New stuff I learned using the scikit learn and SciPy modules.

## Table of Contents

* [Working with Numpy](#working-with-numpy)
    * [Numpy Create Range of Values with The Given Interval](#numpy-create-range-of-values-with-the-given-interval)
    * [Numpy Create Coordinate Matrices from Coordinate Vectors](#numpy-create-coordinate-matrices-from-coordinate-vectors)
    * [Flatten Numpy Array](#flatten-numpy-array)
    * [Pairing Array Values with Second Axis](#pairing-array-values-with-second-axis)
    * [Generate Coordinates Across The Grid](#generate-coordinates-across-the-grid)
* [Plotting](#plotting)
    * [Plot The Surface Decision](#plot-the-surface-decision)
    * [Scatter Plot](#scatter-plot)
* [Dealing with Data](#dealing-with-data)
    * [Deserializing Python Object](#deserializing-python-object)
    * [Split Data for Training and Testing](#split-data-for-training-and-testing)
    * [Vectorized the Strings](#vectorized-the-strings)
    * [Feature Selection](#feature-selection)

## Working with Numpy

### Numpy Create Range of Values with The Given Interval

Use [`arange`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html) to create an array with evenly spaced interval.

```py
import numpy as np

np.arange(0, 5, 1)
# array([0,1,2,3,4])

np.arange(1, 4, 0.5)
# array([1. , 1.5, 2. , 2.5, 3. , 3.5])
```

### Numpy Create Coordinate Matrices from Coordinate Vectors

We can use Numpy [`meshgrid`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html) function to make coordinate matrices from one-dimentional coordinate arrays.

```py
import numpy as np

np.meshgrid([1, 2, 3], [0, 7])
# [
#   array([[1,2,3], [1,2,3]]),
#   array([[0,0,0], [7,7,7]])
# ]
```

### Flatten Numpy Array

When we have a multi-dimensional Numpy array, we can easily flatten it with [`ravel`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html) method:

```py
import numpy as np

arr = np.array([[1,2], [3,4]])
arr.ravel()
# array([1, 2, 3, 4])
```

### Pairing Array Values with Second Axis

We can use Numpy `c_` function to pair array values with another array that will be it's second axis. Read the [`numpy.c_` documentation].

```py
import numpy as np

x = [1,2]
y = [10,20]

np.c_[x, y]
# array([1,10], [2,20])
```

### Generate Coordinates Across The Grid

With the knowledge of Numpy [`arange`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html), [`meshgrid`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html), [`ravel`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html) and [`c_`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.c_.html) functions, we can easily generate coordinates across the grid so we can pass it to the clasifier and plot the decision surface.

```py
import numpy as np

# Generate an evenly spaced coordinates.
x_points, y_points = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

# Pair the x and y points.
test_coordinates = np.c_[x_points.ravel(), y_points.ravel()]
```

## Plotting

### Plot The Surface Decision

We can pass the coordinates across the grid to the clasifier to predict the output on each coordinate. We can then use [`matplotlib.pyplot`](https://matplotlib.org/api/pyplot_api.html) to plot the surface decision.

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

The classifier output would be one dimensional array, so don't forget to [`reshape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html) it back into two dimensional array before plotting. The `cmap` is optional parameter for the color map. Here we use the `seismic` color map from `pylab` module. It has the red-blue colors.

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

## Dealing with Data

### Deserializing Python Object

We can use [`pickle`](https://docs.python.org/2/library/pickle.html) module for serializing and deserializing Python object. There's also the `cPickle`, the faster C implementation. We use both of these modules to deserialize the email text and author list.

```py
import pickle
import cPickle

# Unpickling or deserializing the texts.
texts_file_handler = open(texts_file, "r")
texts = cPickle.load(texts_file_handler)
texts_file_handler.close()

# Unpickling or deserializing the authors.
authors_file_handler = open(authors_file, "r")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()
```

### Split Data for Training and Testing

We can use the built in [`train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) function from scikit-learn to split the data both for training and testing.

```py
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(texts, authors, test_size = 0.1, random_state = 42)
```

`test_size` is the proportion of data to split into the test, on our case we split 10% for testing.

### Vectorized the Strings

When working with text document, we need to vectorize the strings into list of numbers so it's easier to process. We can use the [`TfidfVectorizer`](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) class to vectorize the strings into a matrix of TF-IDF features.

```py
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5, stop_words = "english")
features_train_transformed = vectorizer.fit_transform(features_train)
features_test_transformed = vectorizer.transform(features_test)
```

Word with frequency higher than the `max_df` will be ignored. Stop words are also ignored, these are the most common words in a language (e.g. a, the, has).

### Feature Selection

Text can have a lot of features thus it may slow to compute. We can use scikit [`SelectPercentile`](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html) class to select only important features.

```py
selector = SelectPercentile(f_classif, percentile = 10)
selector.fit(features_train_transformed, labels_train)
selected_features_train_transformed = selector.transform(features_train_transformed).toarray()
selected_features_test_transformed = selector.transform(features_test_transformed).toarray()
```

`percentile` is the percentage of features we'd like to select based on its highest score.
