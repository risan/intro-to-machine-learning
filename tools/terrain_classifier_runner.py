# coding: utf-8
from terrain_data_generator import generate_terrain_data
from plot import predict_and_plot

def run_terrain_classifier(classifier, image_path = None, accuracy_prefix = "🤖 Accuracy: "):
    # Generate a random terrain data.
    features_train, features_test, labels_train, labels_test = generate_terrain_data()

    # Create and train the classifier.
    classifier.fit(features_train, labels_train)

    # Calculate the accuracy.
    accuracy = classifier.score(features_test, labels_test)
    print(accuracy_prefix + str(accuracy))

    # Predict the labels and plot the result.
    predict_and_plot(classifier, features_test, labels_test, image_path)
