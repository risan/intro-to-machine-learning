# Tools

Various tools for supporting this project.

## Table of Contents

* [Modules Breakdown](#modules-breakdown)
    * [The Startup Script](#the-startup-script)
    * [Modules Checker](#modules-checker)
    * [Enron Dataset Downloader](#enron-dataset-downloader)
    * [Email Pre-processor](#email-pre-processor)
        * [Deserializing Python Object](#deserializing-python-object)
        * [Split Data for Training and Testing](#split-data-for-training-and-testing)
        * [Vectorized the Strings](#vectorized-the-strings)
        * [Feature Selection](#feature-selection)
        * [Import Module in Parent Directory](#import-module-in-parent-directory)
    * [Timer](#timer)
* [Python Stuff](#python-stuff)
    * [Import Python Module Dynamically](#import-python-module-dynamically)
    * [Print The Emojis](#print-the-emojis)
    * [Working with Pathname](#working-with-pathname)
    * [Downloading File](#downloading-file)
    * [Extracting Tar File](#extracting-tar-file)

## Modules Breakdown

## The Startup Script

The `startup.py` script will check if all the required packages are installed. It will also download the Enron dataset.

```shell
$ python tools/startup.py
```

## Modules Checker

The `modules_checker.py` is a module that you can use to check if the given module names are installed.

```py
from modules_checker import check_modules

check_modules(["nltk", "numpy", "scipy", "sklearn"])
```

If all the given modules are installed, you'll get the output similar to this:

```shell
✅ nltk is installed.
✅ numpy is installed.
✅ scipy is installed.
✅ sklearn is installed.
```

If one of the given modules are not available, it will stop the script execution.

```shell
✅ nltk is installed.
❌ Please install numpy first.
```

## Enron Dataset Downloader

The `enron_dataset_downloader.py` is a module that we can use to download the Enron dataset:

```py
import os.path
from enron_dataset_downloader import download_enron_dataset

# Pass the absolute path to the directory where you want to store the dataset to.
download_enron_dataset(os.path.abspath('../data'))
```

## Email Pre-processor

The `email_pre_processor.py` is used to split the emails data for training and testing. It will also vectorized the words into list of numbers and select only 10% of features with the highest score.

```py
# coding: utf8
import sys
sys.path.append("../../tools")

from email_pre_processor import pre_process_email

features_train, features_test, labels_train, labels_test = pre_process_email()
```

### Deserializing Python Object

We can use `pickle` module for serializing and deserializing Python object. There's also the `cPickle`, the faster C implementation. We use both of these modules to deserialize the email text and author list.

```py
import pickle
import cPickle

# Unpickling or deserializing the texts.
texts_file_handler = open(texts_file, "r")
texts = cPickle.load(texts_file_handler)
texts_file_handler.close()

# Unpickling or deserializing the authors.
authors_file_handler = open(authors_file, "r")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()
```

### Split Data for Training and Testing

We can use the built in `train_test_split` function from scikit-learn to split the data both for training and testing.

```py
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(texts, authors, test_size = 0.1, random_state = 42)
```

`test_size` is the proportion of data to split into the test, on our case we split 10% for testing.

### Vectorized the Strings

We also need to vectorize the strings into list of numbers so it's easier to process. We use the `TfidfVectorizer` class to vectorize the strings into a matrix of TF-IDF features.

```py
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5, stop_words = "english")
features_train_transformed = vectorizer.fit_transform(features_train)
features_test_transformed = vectorizer.transform(features_test)
```

Word with frequency higher than the `max_df` will be ignored. Stop words are also ignored, these are the most common words in a language (e.g. a, the, has).

### Feature Selection

Text can have a lot of features thus it may slow to compute. We can use scikit `SelectPercentile` class to select only important features.

```py
selector = SelectPercentile(f_classif, percentile = 10)
selector.fit(features_train_transformed, labels_train)
selected_features_train_transformed = selector.transform(features_train_transformed).toarray()
selected_features_test_transformed = selector.transform(features_test_transformed).toarray()
```

`percentile` is the percentage of features we'd like to select based on its highest score.

### Import Module in Parent Directory

This `email_pre_processor` module is used on other modules outside this directory. To include other modules on parent directory we first need to add the directory with `sys.path.append`:

```py
import sys
sys.path.append("../../tools")

from email_pre_processor import pre_process_email
```

## Timer

The `timer.py` contain a `Timer` class with two static methods to count the time:

```py
from timer import Timer

Timer.start()
# Do some thing here
Timer.stop("Time: ") # Time: 1.234s
```

## Python Stuff

### Import Python Module Dynamically

We can dynamically import a Python module using the `__import__` function:

```py
module_name = "numpy"

__import__(module_name)
```

### Print The Emojis

To print the emojis or any other unicode characters in Python, we have to declare the encoding type like this:

```py
# coding: utf8

print("😅")
```

### Working with Pathname

Get the filename from the given URL:

```py
import os
from urlparse import urlparse

url = "https://example.com/foo.txt"

url_components = urlparse(url)

filename = os.path.basename(url_components.path) # foo.txt
```

Check if the given file path is exists:

```py
import os

is_exists = os.path.isfile("foo.txt")
```

Create the directory if it's not exists:

```py
import os
import errno

try:
    os.makedirs(directory_path)
except OSError, e:
    if e.errno != errno.EEXIST:
        raise
```

### Downloading File

We can use the `urllib` module to download a file in Python. The first argument is the file URL, and the second argument is an optional filename that will be used to save the file.

```py
import urllib

urllib.urlretrieve("https://example.com/foo.txt", "foo.txt")
```

### Extracting Tar File

There's `tarfile` module that we can use to deal with Tar file in Python. To extract the `tar.gz` file we can use the following code:

```py
import tarfile

# Open the file.
tfile = tarfile.open("foo.tar.gz")

# Extract the file to the given path.
tfile.extractall(path)
```

We can pass the `mode` parameter to the `open` method. By default the `mode` would be `r`—reading mode with transparent compression. There are also other mode options:

* `r:gz`: Reading mode with gzip compression.
* `r:`: Reading mode without compression.
* `a`: Appending mode without compression.
* `w`: Writting mode without compression.
* Checkout other available options in [tarfile documentation](https://docs.python.org/2/library/tarfile.html)
