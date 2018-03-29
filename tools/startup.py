# coding: utf8
import os.path
from modules_checker import check_modules
from enron_dataset_downloader import download_enron_dataset

check_modules(["nltk", "numpy", "scipy", "sklearn"])

download_enron_dataset(os.path.abspath('../data'))

print "🎉 You're ready to go!"
