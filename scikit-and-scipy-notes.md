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

## Working with Numpy

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

## Plotting

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
