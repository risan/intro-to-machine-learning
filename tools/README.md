# Tools

Various tools for supporting this project.

## Available Modules

* [Using Modules in Tools Directory](#using-modules-in-tools-directory)
* [The Startup Script](#the-startup-script)
    * [Modules Checker](#modules-checker)
    * [Enron Dataset Downloader](#enron-dataset-downloader)
* [Terrain Classifier Runner](#terrain-classifier-runner)
    * [Terrain Data Generator](#terrain-data-generator)
    * [Predict and Plot](#predict-and-plot)
* [Email Classifier Helpers](#email-classifier-helpers)
    * [Email Pre-processor](#email-pre-processor)
        * [Deserializing Python Object](#deserializing-python-object)
        * [Split Data for Training and Testing](#split-data-for-training-and-testing)
        * [Vectorized the Strings](#vectorized-the-strings)
        * [Feature Selection](#feature-selection)
    * [Timer](#timer)

## Using Modules in Tools Directory

Many of the modules here are used by the other modules outside this `tool` directory.
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

check_modules(["nltk", "numpy", "scipy", "sklearn", "matplotlib])
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

# Pass the absolute path to the directory where you want to store the dataset to.
download_enron_dataset("/path/to/data_directory")
```

## Terrain Classifier Runner

The `terrain_classifier_runner.py` is module that we can use easily run the various classifier and run it agains the terrain data. It will automatically train the given classifier, calculate the accuracy, predict the test data and plot the result.

All we have to do is pass the `classifier` instance as the first argument. The second `image_path` argument is optional, this the path where you want to save the plot image. The `accuracy_prefix` is also optional, it's the text that you want to display right before the accuracy score.

```py
from sklearn.naive_bayes import GaussianNB
from terrain_classifier_runner import run_terrain_classifier

# Create the classifier.
classifier = GaussianNB()

# Run the classifier.
run_terrain_classifier(classifier, image_path = "plot.png", accuracy_prefix = "🤖 Accuracy: ")
```

### Terrain Data Generator

The `terrain_data_generator.py` is used to generate a random terrain data. It accepts the optional `total_points` parameter, which determines the total number of points that needs to be generated (default to `1000`).

```py
from terrain_data_generator import generate_terrain_data

features_train, features_test, labels_train, labels_test = generate_terrain_data(total_points = 1000)
```

### Predict and Plot

The `plot.py` module is used to run the classifier and plot the prediction result.

```py
from plot import predict_and_plot

predict_and_plot(classifier, features_test, labels_test, image_path)
```

* `classifier`: It's an instance of the trained classifier.
* `features_test`: The features test to predict.
* `labels_test`: The actual output labels.
* `iamge_path`: The optional image path, pass this parameter if you want to save the plot as an image too.

## Email Classifier Helpers

### Email Pre-processor

The `email_pre_processor.py` is used to split the emails data for training and testing. It will also vectorized the words into list of numbers and select only 10% of features with the highest score.

```py
from email_pre_processor import pre_process_email

features_train, features_test, labels_train, labels_test = pre_process_email()
```

It accepts two optional parameters:

- `texts_file`: The path to the email text list file.
- `authors_file`: The path to the email author list file.

### Timer

The `timer.py` contain a `Timer` class with two static methods to count the time:

```py
from timer import Timer

Timer.start()
# Do some thing here
Timer.stop("Time: ") # Time: 1.234s
```
