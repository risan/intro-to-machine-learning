# coding: utf-8
"""Exploring Enron Dataset"""
import os
import sys

def data_path(path):
    """Get the full data path.

    :param str path: The data path
    :return: The full path to the given data path
    :rtype: str
    """
    dirname = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.abspath(os.path.join(dirname, "../../data"))

    return os.path.join(data_dir, path)

import pickle

file_handler = open(data_path("enron_people.pkl"), "r")
enron_people = pickle.load(file_handler)
file_handler.close()

print("🏢 Total numbers of people: " + str(len(enron_people)))
print("🌈 Total numbers of features: " + str(len(enron_people["SKILLING JEFFREY K"])))

total_poi = sum([person["poi"] for person in enron_people.itervalues()])
print("🤡 Total people of interest: " + str(len(enron_people)))
