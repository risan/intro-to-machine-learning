# coding: utf-8
from terrain_data_generator import generate_terrain_data
from terrain_classifier_plotter import plot

def run_terrain_classifier(classifier, image_path = None, title = None):
    # Print the title if any.
    if title: print(title)

    # Generate a random terrain data.
    features_train, features_test, labels_train, labels_test = generate_terrain_data()

    # Create and train the classifier.
    classifier.fit(features_train, labels_train)

    # Calculate the accuracy.
    accuracy = classifier.score(features_test, labels_test)
    print("🤖 Accuracy: " + str(accuracy) + "\n")

    # Plot the decision boundary and test data.
    plot(classifier, features_test, labels_test, image_path)
