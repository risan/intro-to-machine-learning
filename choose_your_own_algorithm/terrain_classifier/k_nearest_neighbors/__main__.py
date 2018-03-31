# coding: utf-8
"""Terrain classifier with K-Nearest Neighbors"""
import os
import sys

# Append the tools directory. Use the absolute path to tools directory so we
# can run this file even outside its directory.
dirname = os.path.dirname(os.path.realpath(__file__))
tools_path = os.path.abspath(os.path.join(dirname, "../../../tools"))
sys.path.append(tools_path)

from sklearn.neighbors import KNeighborsClassifier
from terrain_classifier_runner import run_terrain_classifier

# Create the classifier.
classifier = KNeighborsClassifier(n_neighbors = 10, weights = "distance")

# Run the classifier.
run_terrain_classifier(classifier, os.path.join(dirname, "n_neighbors10_weight_distance.png"))
