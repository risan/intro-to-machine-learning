# coding: utf8
import os.path
from modules_checker import check_modules
from enron_dataset_downloader import download_enron_dataset

dirname = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.abspath(os.path.join(dirname, "../data"))

# Make sure that all of these modules are installed.
check_modules(["nltk", "numpy", "scipy", "sklearn", "matplotlib"])

# Download the Enron data set.
download_enron_dataset(os.path.realpath(data_path))

print "🎉 You're ready to go!"
