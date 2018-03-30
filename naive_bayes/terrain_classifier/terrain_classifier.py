# coding: utf-8
"""Terrain classifier with Naive Bayes"""
import os
import sys

# Append the tools directory. Use the absolute path to tools directory so we
# can run this file even outside its directory.
dirname = os.path.dirname(os.path.realpath(__file__))
tools_path = os.path.abspath(os.path.join(dirname, "../../tools"))
sys.path.append(tools_path)

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
predict_and_plot(classifier, features_test, labels_test, image_path = os.path.join(dirname, "plot.png"))
