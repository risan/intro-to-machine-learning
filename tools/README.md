# Tools

Various tools for supporting this project.

## Table of Contents

* [Modules Breakdown](#modules-breakdown)
    * [The Startup Script](#the-startup-script)
    * [Modules Checker](#modules-checker)
    * [Enron Dataset Downloader](#enron-dataset-downloader)
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
