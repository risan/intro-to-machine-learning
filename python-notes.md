# Python Notes

I rarely use Python before. Here are new things I've discovered on Python while learning this machine learning course.

## Table of Contents

* [Modules Classes and Functions](#modules-classes-and-functions)
    * [Import Python Module Dynamically](#import-python-module-dynamically)
    * [Multiple Returns in Python](#multiple-returns-in-python)
    * [Importing Modules Outside of the Directory](importing-modules-outside-of-the-directory)
* [Output](#output)
    * [Print The Emojis](#print-the-emojis)
    * [Pretty Print](#pretty-print)
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
    * [Sort List in Ascending Order](#sort-list-in-ascending-order)
    * [Using Filter with List](#using-filter-with-list)
    * [Using Reduce with List of Dictionary](#using-reduce-with-list-of-dictionary)
* [Working with Dictionary](#working-with-dictionary)
    * [Loop Through Dictionary](#loop-through-dictionary)
    * [Calculate Total of Particular Dictionary Key](#calculate-total-of-particular-dictionary-key)

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

## Importing Modules Outside of the Directory

In order to import modules from outside of the directory, we need to add that module's directory with `sys.path.append`. Suppose we have the following directory structure:

```py
|--foo
| |-- bar.py
|
|-- tools
| |-- speak_yoda.py
```

If we want to use the `speak_yoda.py` module within the `bar.py`, we can do the following:

```py
# /foo/bar.py
import os

sys.path.append("../tools")

import speak_yoda
```

However this won't work if you run the `baz.py` file from outside of its `foo` directory:

```shell
# Works inside the /foo directory.
$ cd /foo
$ python bar.py

# Won't work if it's on its project root directory.
$ python foo/bar.py
```

To solve this we can append the `tools` directory using it's absolute path.

```py
# /foo/bar.py
import os
import sys

# Get the directory name for this file.
current_dirname = os.path.dirname(os.path.realpath(__file__))

# Use the absolute path to the tools directory
tools_path = os.path.abspath(os.path.join(dirname, "../tools"))
sys.path.append(tools_path)

import speak_yoda
```

## Output

### Print The Emojis

To print the emojis or any other unicode characters in Python, we have to declare the encoding type at the top like this:

```py
# coding: utf8

print("😅")
```

### Pretty Print

Print Python data structure nicely with configurable indentation:

```py
import pprint
pp = pprint.PrettyPrinter(indent=2)

pp.pprint(people)
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

### Sort List in Ascending Order

We can sort a list in ascending order by calling the `sort` method.

```py
people = ["John", "Alice", "Poe"]
people.sort()
print(people) # ["Alice", "John", "Poe"]
```

### Using Filter with List

Just like its name, we can use `filter` to filter our list:

```py
numbers = range(1, 11)

even_numbers = filter(lambda number: number % 2 == 0, numbers)
# [2, 4, 6, 8, 10]
```

We can break the above statement into two parts:

- `lambda number: statement`: `number` is the variable name we'd like to use to refrence a single item from the `numbers` list. The following statement must evaluate to truthy/falsy value—falsy means the current item will be removed from the final result.
- `numbers`: The second parameter is the list we'd like to filter.

### Using Reduce with List of Dictionary

We can use the `reduce` function to find the total of particular key in a list of dictionary:

```py
items = [{value:10}, {value:20}, {value:50}]

# Find the total of value key.
totalValues = reduce(lambda total, item: total + item["value"], items, 0) # 80
```

It can be broken down into 4 parts:
- `lambda total`: It's the carried/accumulative value that will finally be returned.
- `item: statement`: `item` is the name of variable we'd like to use to reference the single item from the `items` list. The statement to execute in order to define the accumulative value for the next iteration.
- `items`: It's the list of item that we would like to "reduce"
- `0`: The last parameter is optional, it's the initial accumulative value for the first iteration.

We can also use `reduce` function to find a single item from the list. Here's an example to find the person with the biggest `total_payments` within the given list of people dictionary.

```py
people = [
    {"name": "John", "total_payments": 100},
    {"name": "Alice", "total_payments": 1000},
    {"name": "Poe", "total_payments": 800}
]

person_biggest_total_payments = reduce(lambda paid_most, person: person if person["total_payments"] > paid_most["total_payments"] else paid_most, people, { "total_payments": 0 })
# {'name': 'Alice', 'total_payments': 1000}
```

## Working with Dictionary

### Loop Through Dictionary

We can use the `itervalues` method to loop through a dictionary:

```py
for person in people.itervalues():
    print(person["email_address"])
```

You can also use the `iteritems` if you want to access the key too:

```py
for person in people.iteritems():
    print(person[0] + ": " + person[1]["email_address"])
```

### Calculate Total of Particular Dictionary Key

Suppose we want to calculate the total of `sallary` key on a `people` dictionary:

```py
total_salary = sum([person["salary"] for person in people.itervalues()])
```
