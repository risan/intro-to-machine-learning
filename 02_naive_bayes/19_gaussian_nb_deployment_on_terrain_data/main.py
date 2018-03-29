"""Naive Bayes classifier
Use sklearn Naive Bayes classifier to classify terrain data and plot the
decision boundary.
"""
from terrain_data_generator import generateTerrainData
from nb_classifier import trainClassifier
from plot import predictAndPlot

# Generate a random terrain data.
features_train, labels_train, features_test, labels_test = generateTerrainData()

# Train the classifier.
classifier = trainClassifier(features_train, labels_train)

# Predict the labels and plot the result.
predictAndPlot(classifier, features_test, labels_test)
