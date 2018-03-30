# Tools

Various tools for supporting this project.

## Available Modules

* [Using Modules in Tools Directory](#using-modules-in-tools-directory)
* [The Startup Script](#the-startup-script)
    * [Modules Checker](#modules-checker)
    * [Enron Dataset Downloader](#enron-dataset-downloader)
* [Terrain Classifier Runner](#terrain-classifier-runner)
    * [Terrain Data Generator](#terrain-data-generator)
    * [Terrain Classifier Plotter](#terrain-classifier-plotter)
* [Email Classifier Runner](#email-classifier-runner)
    * [Email Pre-processor](#email-pre-processor)
        * [Deserializing Python Object](#deserializing-python-object)
        * [Split Data for Training and Testing](#split-data-for-training-and-testing)
        * [Vectorized the Strings](#vectorized-the-strings)
        * [Feature Selection](#feature-selection)
    * [Timer](#timer)

## Using Modules in Tools Directory

Many of the modules here are used by the other modules outside of this `tools` directory.
To import and use these modules outside of the `tool` directory, we need to use `sys.path.append` first:

```py
import sys
sys.path.append("/path/to/tools")

from terrain_data_generator import generate_terrain_data
```

## The Startup Script

The `startup.py` script will check if all the required packages are installed. It will also download the Enron dataset.

```shell
$ python tools/startup.py
```

### Modules Checker

The `modules_checker.py` is a module that you can use to check if the given module names are installed.

```py
from modules_checker import check_modules

check_modules(names)
```

**Parameters:**

* `names`: List of module names to check.

Usage example:

```py
from modules_checker import check_modules

check_modules(["nltk", "numpy", "scipy", "sklearn", "matplotlib"])
```

If all the given modules are installed, you'll get the output similar to this:

```shell
✅ nltk is installed.
✅ numpy is installed.
✅ scipy is installed.
✅ sklearn is installed.
✅ matplotlib is installed.
```

If one of the given modules are not available, it will stop the script execution.

```shell
✅ nltk is installed.
❌ Please install numpy first.
```

### Enron Dataset Downloader

The `enron_dataset_downloader.py` is a module that we can use to download the Enron dataset:

```py
from enron_dataset_downloader import download_enron_dataset

download_enron_dataset(directory)
```

**Parameters:**

* `directory`: The path to the directory where you want to store the dataset to.

## Terrain Classifier Runner

The `terrain_classifier_runner.py` is module that we can use to run the classifier against the terrain data. It will automatically train the given classifier, calculate the accuracy, predict the output test labels and plot the result.

```py
from terrain_classifier_runner import run_terrain_classifier

run_terrain_classifier(classifier, [image_path = None], [title = None])
```

**Parameters:**

* `classifier`: This is the classifier object that you want to run.
* `image_path`: This is the optional path where you want to save the plot image to. If not given, it won't save any plot image.
* `title`: This is the optional text that you want to print before running the classifier.

Usage example:

```py
from sklearn.naive_bayes import GaussianNB
from terrain_classifier_runner import run_terrain_classifier

# Create the classifier.
classifier = GaussianNB()

# Run the classifier.
run_terrain_classifier(classifier, image_path = "plot.png", title = "Gaussian Naive Bayes")
```

### Terrain Data Generator

The `terrain_data_generator.py` is used to generate a random terrain data. It returns 4 lists of features and labels with the following order:

1. List of features for training
2. List of features for testing
3. List of labels for training
4. List of labels for testing

```py
from terrain_data_generator import generate_terrain_data

features_train, features_test, labels_train, labels_test = generate_terrain_data([total_points = 1000])
```

**Parameters**

* `total_points`: Total number of points to generate (default to 1000).

Usage example:

```py
from terrain_data_generator import generate_terrain_data

features_train, features_test, labels_train, labels_test = generate_terrain_data(1000)
```

### Terrain Classifier Plotter

The `terrain_classifier_plotter.py` module is used to run the classifier and plot both the decision boundary and the test points.

```py
from terrain_classifier_plotter import plot

plot(classifier, features_test, labels_test, [image_path = None])
```

* `classifier`: It's an instance of the trained classifier.
* `features_test`: The features test to predict.
* `labels_test`: The actual output labels.
* `image_path`: The optional image path, pass this parameter if you want to save the plot as an image too.

## Email Classifier Runner

The `email_classifier_runner.py` is module that we can use to run the classifier against the email data. It will automatically train the given classifier, predict the output test labels, and calculate the accuracy. It will also count the time it takes in training and prediction phase. This function also returns a list of the predicted output labels.

```py
from email_classifier_runner import run_email_classifier

run_email_classifier(classifier, [title = None], [training_data_proportion = 1])
```

**Parameters:**

* `classifier`: This is the classifier object that you want to run.
* `title`: This is the optional text that you want to print before running the classifier.
* `training_data_proportion`: The proportion of training data to use, default to `1`. Note that this is not the proportion of training data againsts the testing data. But simply the proportion of testing data that will be feed to the classifier. Use the value `< 1` to drop some of the testing data thus speeding up the training and predicting processes.

Usage example:

```py
from sklearn.naive_bayes import GaussianNB
from email_classifier_runner import run_email_classifier

# Create the classifier.
classifier = GaussianNB()

# Run the classifier.
labels_prediction = run_email_classifier(classifier)
```

### Email Pre-processor

The `email_pre_processor.py` is used to split the emails data for training and testing. It will also vectorized the words into list of numbers and select only 10% of features with the highest score. It will return 4 lists of features and labels in the following order:

1. List of features for training
2. List of features for testing
3. List of labels for training
4. List of labels for testing

```py
from email_pre_processor import pre_process_email

features_train, features_test, labels_train, labels_test = pre_process_email([texts_file = "/path/to/data/email/texts.pkl", author_text = "/path/to/data/email/authors.pkl"])
```

It accepts two optional parameters:

- `texts_file`: The path to file that holds the serialized list of email texts. It defaults to the absolute path of `/email/texts.pkl` file in `data` directory.
- `authors_file`: The path to file that holds the serialized list of authors texts. It defaults to the absolute path of `/email/authors.pkl` file in `data` directory.

### Timer

The `timer.py` contain a `Timer` class with two static methods to count the time:

```py
from timer import Timer

Timer.start()
# Do some thing here
Timer.stop("Time: ") # Time: 1.234s
```
