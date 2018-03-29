import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

def predict_and_plot(classifier, features_test, labels_test):
    """Predict the output labels and plot both the test points and decision boundary.

    :param obj classifier: The classifier instance
    :param list features_test: The features to predict
    :param list labels_test: The actual labels
    """
    x_min = 0.0
    x_max = 1.0
    y_min = 0.0
    y_max = 1.0

    step = 0.01 # Step size in the mesh.
    x_points, y_points = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    # Combine the x & y points and predict the output.
    predicted_labels = classifier.predict(np.c_[x_points.ravel(), y_points.ravel()])

    # Reshape the array dimenson to match x_points.
    predicted_labels = predicted_labels.reshape(x_points.shape)

    # Set the axes limit.
    plt.xlim(x_points.min(), x_points.max())
    plt.ylim(y_points.min(), y_points.max())

    # Plot the decision boundary with seismic color map.
    plt.pcolormesh(x_points, y_points, predicted_labels, cmap = pl.cm.seismic)

    # Separate fast (label = 0) & slow (label = 1) test points.
    grade_fast = [features_test[i][0] for i in range(0, len(features_test)) if labels_test[i] == 0]
    bumpy_fast = [features_test[i][1] for i in range(0, len(features_test)) if labels_test[i] == 0]
    grade_slow = [features_test[i][0] for i in range(0, len(features_test)) if labels_test[i] == 1]
    bumpy_slow = [features_test[i][1] for i in range(0, len(features_test)) if labels_test[i] == 1]

    # Plot the test points.
    plt.scatter(grade_fast, bumpy_fast, color = "b", label = "fast")
    plt.scatter(grade_slow, bumpy_slow, color = "r", label = "slow")

    # Show the plot
    plt.legend()
    plt.xlabel("grade")
    plt.ylabel("bumpiness")
    plt.show()
