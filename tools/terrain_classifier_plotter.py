import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

def plot(classifier, features_test, labels_test, image_path = None):
    """Plot the decision boundary and the test points for terrain classifier.

    :param obj classifier: The classifier instance
    :param list features_test: The features to predict
    :param list labels_test: The actual labels
    :param str image_path: The path where the plot image will be saved
    """
    x_min = 0.0
    x_max = 1.0
    y_min = 0.0
    y_max = 1.0

    step = 0.01 # Step size in the mesh.
    x_points, y_points = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    # Combine the x & y points and predict the output.
    label_predictions = classifier.predict(np.c_[x_points.ravel(), y_points.ravel()])

    # Reshape the array dimenson to match x_points.
    label_predictions = label_predictions.reshape(x_points.shape)

    # Set the axes limit.
    plt.xlim(x_points.min(), x_points.max())
    plt.ylim(y_points.min(), y_points.max())

    # Plot the decision boundary with seismic color map.
    plt.pcolormesh(x_points, y_points, label_predictions, cmap = pl.cm.seismic)

    # Separate fast (label = 0) & slow (label = 1) test points.
    grade_fast = [features_test[i][0] for i in range(0, len(features_test)) if labels_test[i] == 0]
    bumpy_fast = [features_test[i][1] for i in range(0, len(features_test)) if labels_test[i] == 0]
    grade_slow = [features_test[i][0] for i in range(0, len(features_test)) if labels_test[i] == 1]
    bumpy_slow = [features_test[i][1] for i in range(0, len(features_test)) if labels_test[i] == 1]

    # Plot the test points.
    plt.scatter(grade_fast, bumpy_fast, color = "b", label = "fast")
    plt.scatter(grade_slow, bumpy_slow, color = "r", label = "slow")

    plt.legend()
    plt.xlabel("grade")
    plt.ylabel("bumpiness")

    # Save the plot to file.
    if image_path:
        plt.savefig(image_path)

    # Show the plot
    plt.show()
