from sklearn.naive_bayes import GaussianNB

def trainClassifier(features_train, labels_train):
    """Create and train Gaussian Naive Bayes classifier.

    :param list features_train: The features input for training
    :param list labels_train: The labels output for training
    :return: The GaussianNB classifier instance
    :rtype: sklearn.naive_bayes.GaussianNB
    """
    classifier = GaussianNB()
    classifier.fit(features_train, labels_train)

    return classifier
