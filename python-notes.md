# Python Notes

I rarely use Python before. Here are new things I've discovered on Python while learning this machine learning course.

## Table of Contents

* [Modules Classes and Functions](#modules-classes-and-functions)
    * [Import Python Module Dynamically](#import-python-module-dynamically)
    * [Multiple Returns in Python](#multiple-returns-in-python)
* [Print The Emojis](#print-the-emojis)
* [Working with Pathname](#working-with-pathname)
    * [Get Filename From URL](#get-filename-from-url)
    * [Check if File Exists](#check-if-file-exists)
    * [Create a Directory if It's Not Exists](#create-a-directory-if-its-not-exists)
* [Working with Files](#working-with-files)
    * [Downloading File](#downloading-file)
    * [Extracting Tar File](#extracting-tar-file)
* [Working with List](#working-with-list)
    * [Generate a List of Random Numbers](#generate-a-list-of-random-numbers)
    * [Pair Values from Two Lists](#pair-values-from-two-lists)
    * [Splitting a List](#splitting-a-list)
    * [Filtering List In One Line](#filtering-list-in-one-line)

## Modules Classes and Functions

### Main Entry File

Suppose our Python project is stored in `/foo/bar` directory. And this application has one file that servers as the single entry point. We can name this file `__main__.py` so we can run this project simply be referencing it's directory path:

```py
$ python /foo/bar

# It's equivalent to this
$ python /foo/bar/__main__.py
```

### Import Python Module Dynamically

We can dynamically import a Python module using the [`__import__`](https://docs.python.org/2/library/functions.html#__import__) function:

```py
module_name = "numpy"

__import__(module_name)
```

## Multiple Returns in Python

In Python we can return multiple values seperated by commas.

```py
def test():
    return 100, "foo"

someNumber, someString = test()
```

## Print The Emojis

To print the emojis or any other unicode characters in Python, we have to declare the encoding type at the top like this:

```py
# coding: utf8

print("😅")
```

## Working with Pathname

Read the [`os.path` documentation](https://docs.python.org/2/library/os.path.html).

### Get Filename From URL

We can extract a filename from the given URL:

```py
import os
from urlparse import urlparse

url = "https://example.com/foo.txt"

url_components = urlparse(url)

filename = os.path.basename(url_components.path) # foo.txt
```

### Check if File Exists

To check if the given file path is exists or not:

```py
import os

is_exists = os.path.isfile("foo.txt")
```

### Create a Directory if It's Not Exists

To create a directory if it's not exists:

```py
import os
import errno

try:
    os.makedirs(directory_path)
except OSError, e:
    if e.errno != errno.EEXIST:
        raise
```

## Working with Files

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

## Working with List

### Generate a List of Random Numbers

Use the `for..in` syntax to generate a list of random numbers in one line.

```py
import random

# Initialize internal state of random generator.
random.seed(42)

# Generate random points.
randomNumbers = [random.random() for i in range(0, 10)]
# [0.6394267984578837, 0.025010755222666936, 0.27502931836911926, ...]
```

### Pair Values from Two Lists

The built-in `zip` function can pair values from two lists, but it will return a list of tuples. To get a list of value pairs, we can combine it with `for..in`:

```py
coordinates = [[x, y] for x,y in zip([5,10,15], [0,1,0])]
# [[5, 0], [10, 1], [15, 0]]
```

### Splitting a List

We can easily split a list in Python by specifying the starting index and it's ending index. The ending index is excluded. You can specify a negative index. And both of these indices are optional.

```py
a = [0,1,2,3,4,5]

a[0:3]  # 0,1,2
a[1:3]  # 1,2
a[2:]   # 2,3,4,5
a[:3]   # 0,1,2
a[0:-2] # 0,1,2,3
a[-2:]  # 4,5
a[:]    # 0,1,2,3,4,5
```

### Filtering List In One Line

We can easily filter a list by combinning the `for..in` and `if` syntaxs together.

```py
numbers = range(1,11)

# Filter even numbers only.
[numbers[i] for i in range(0, len(numbers)) if numbers[i] % 2 == 0]
# [2, 4, 6, 8, 10]
```
