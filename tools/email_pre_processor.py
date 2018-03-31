import os
import pickle
import cPickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

def data_path(path):
    """Get the full data path.

    :param str path: The data path
    :return: The full path to the given data path
    :rtype: str
    """
    dirname = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.abspath(os.path.join(dirname, "../data"))

    return os.path.join(data_dir, path)

def pre_process_email(texts_file = data_path("email/texts.pkl"), authors_file = data_path("email/authors.pkl"), features_percentile = 10):
    """Pre-process the emails data.

    The texts_file contains the list of email texts and the authors_file
    contains the corresponding authors. This method will perform the following
    tasks:
        -- Split the data 90% for training and 10% for testing
        -- Vectorizes into tfidf matrix
        -- Selects or keeps most helpful features

    :param str texts_file: The path to the email texts file (features)
    :param str authors_file: The path to the email authors file (labels)
    :return: 4 lists of features_train, features_test, labels_train, labels_test
    """
    # Unpickling or deserializing the texts.
    texts_file_handler = open(texts_file, "r")
    texts = cPickle.load(texts_file_handler)
    texts_file_handler.close()

    # Unpickling or deserializing the authors.
    authors_file_handler = open(authors_file, "r")
    authors = pickle.load(authors_file_handler)
    authors_file_handler.close()

    # Split the data for training and testing it will also randomize the order.
    features_train, features_test, labels_train, labels_test = train_test_split(texts, authors, test_size = 0.1, random_state = 42)

    # Vectorized the strings to the list of numbers.
    vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5, stop_words = "english")
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    # Since text can have a lot of features, it can be slow to compute.
    # Select only 10% of the features with the highest score.
    selector = SelectPercentile(f_classif, percentile = features_percentile)
    selector.fit(features_train_transformed, labels_train)
    selected_features_train_transformed = selector.transform(features_train_transformed).toarray()
    selected_features_test_transformed = selector.transform(features_test_transformed).toarray()

    return selected_features_train_transformed, selected_features_test_transformed, labels_train, labels_test
