# coding: utf-8
from sklearn.metrics import accuracy_score
from email_pre_processor import pre_process_email
from timer import Timer

def run_email_classifier(classifier, title = None):
    # Print the title if any.
    if title: print(title)

    # Get the email data.
    features_train, features_test, labels_train, labels_test = pre_process_email()

    # Create and train the classifier.
    Timer.start()
    classifier.fit(features_train, labels_train)
    Timer.stop("⏱ Training time: ")

    # Predict the test features.
    Timer.start()
    labels_prediction = classifier.predict(features_test)
    Timer.stop("⏱ Predicting time: ")

    # Calculate the accuracy.
    accuracy = accuracy_score(labels_test, labels_prediction)
    print("🤖 Accuracy: " + str(accuracy) + "\n")
