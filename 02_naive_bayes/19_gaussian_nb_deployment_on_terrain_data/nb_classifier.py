from sklearn.naive_bayes import GaussianNB

def trainClassifier(features_train, labels_train):
    """Create and train Gaussian Naive Bayes classifier.

    Keyword arguments:
    features_train -- features training input
    labels_train -- training output labels
    """
    classifier = GaussianNB()
    classifier.fit(features_train, labels_train)

    return classifier
