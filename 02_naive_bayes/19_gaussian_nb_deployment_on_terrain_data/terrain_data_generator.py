import random

def generateTerrainData(total_points = 1000):
    """Generate a random terrain data.

    Keyword arguments:
    total_points -- total points to generate (default 1000)
    """
    random.seed(42) # Initialize internal state of random generator.

    # Generate random features.
    gradePoints = [random.random() for i in range(0, total_points)]
    bumpyPoints = [random.random() for i in range(0, total_points)]
    features = [[grade, bumpy] for grade,bumpy in zip(gradePoints, bumpyPoints)]

    # Generate random labels.
    errorPoints = [random.random() for i in range(0, total_points)]
    labels = [round((gradePoints[i] * bumpyPoints[i]) + 0.3 + (0.1 * errorPoints[i])) for i in range(0, total_points)]

    for i in range(0, total_points):
        if gradePoints[i] > 0.8 or bumpyPoints[i] > 0.8:
            labels[i] = 1.0

    # Split for training and testing.
    splitIdx = int(0.75 * total_points)
    features_train = features[0:splitIdx]
    features_test = features[splitIdx:]
    labels_train = labels[0:splitIdx]
    labels_test = labels[splitIdx:]

    return features_train, labels_train, features_test, labels_test
