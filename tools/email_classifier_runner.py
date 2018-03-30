# coding: utf-8
from sklearn.metrics import accuracy_score
from email_pre_processor import pre_process_email
from timer import Timer

def run_email_classifier(classifier, title = None, training_data_proportion = 1):
    # Print the title if any.
    if title: print(title)

    # Get the email data.
    features_train, features_test, labels_train, labels_test = pre_process_email()

    # Cut down the training data.
    if training_data_proportion < 1:
        total_training_data = int(len(labels_train) * training_data_proportion)
        features_train = features_train[:total_training_data]
        labels_train = labels_train[:total_training_data]

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

    # Count total numbers of email from Chris (1) and Sarah (0)
    total_emails_chris = sum(labels_prediction)
    total_emails_sarah = len(labels_prediction) - total_emails_chris
    print("👦 Total emails from Chris: " + str(total_emails_chris))
    print("👧 Total emails from Sarah: " + str(total_emails_sarah) + "\n")

    return labels_prediction
