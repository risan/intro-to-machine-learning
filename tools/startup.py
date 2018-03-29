# coding: utf8
import os.path
from modules_checker import check_modules
from enron_dataset_downloader import download_enron_dataset

# Make sure that all of these modules are installed.
check_modules(["nltk", "numpy", "scipy", "sklearn"])

# Download the Enron data set.
download_enron_dataset(os.path.realpath('../data'))

print "🎉 You're ready to go!"
