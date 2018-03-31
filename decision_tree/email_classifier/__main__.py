# coding: utf-8
import os
import sys

# Append the tools directory. Use the absolute path to tools directory so we
# can run this file even outside its directory.
dirname = os.path.dirname(os.path.realpath(__file__))
tools_path = os.path.abspath(os.path.join(dirname, "../../tools"))
sys.path.append(tools_path)

from sklearn.tree import DecisionTreeClassifier
from email_classifier_runner import run_email_classifier

# Create the classifier.
classifier = DecisionTreeClassifier(min_samples_split = 40)

# Run the classifier with 1% features.
run_email_classifier(classifier, features_percentile = 1)
