import random

def generateTerrainData(total_points = 1000):
    """Generate a random terrain data.

    Keyword arguments:
    total_points -- total points to generate (default 1000)
    """
    random.seed(42) # Initialize internal state of random generator.

    # Generate random data.
    gradePoints = [random.random() for i in range(0, total_points)]
    bumpyPoints = [random.random() for i in range(0, total_points)]
    x = [[grade, bumpy] for grade,bumpy in zip(gradePoints, bumpyPoints)]

    # Generate random output
    errorPoints = [random.random() for i in range(0, total_points)]
    y = [round((gradePoints[i] * bumpyPoints[i]) + 0.3 + (0.1 * errorPoints[i])) for i in range(0, total_points)]

    for i in range(0, total_points):
        if gradePoints[i] > 0.8 or bumpyPoints[i] > 0.8:
            y[i] = 1.0

    # Split for training and testing.
    splitIdx = int(0.75 * total_points)
    x_train = x[0:splitIdx]
    x_test = x[splitIdx:]
    y_train = y[0:splitIdx]
    y_test = y[splitIdx:]

    return x_train, y_train, x_test, y_test
