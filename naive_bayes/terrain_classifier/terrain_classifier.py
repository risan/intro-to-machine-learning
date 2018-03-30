# coding: utf-8
"""Terrain classifier with Naive Bayes"""
import sys

sys.path.append("../../tools")

from sklearn.naive_bayes import GaussianNB
from terrain_data_generator import generate_terrain_data
from plot import predict_and_plot

# Generate a random terrain data.
features_train, features_test, labels_train, labels_test = generate_terrain_data()

# Create and train the classifier.
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Calculate the accuracy.
accuracy = classifier.score(features_test, labels_test)
print("🤖 Accuracy: " + str(accuracy))

# Predict the labels and plot the result.
predict_and_plot(classifier, features_test, labels_test)
