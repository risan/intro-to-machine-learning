# Datasets and Questions

* Uses regression to understand the relationship between salaries and bonuses.
* Uses clustering to identify whose on the board of directors and whose just the regular employees.
* Uses outlier detection to identify and remove bugs on the data.

## Person of Interest

Let's define the criteria of the Person of Interest or POI.

* Indicted (charge with a crime).
* Settled (paid fine) without admitting guilt.
* Testified in exchange of immunity.

## Accuracy vs Training Set Size

The more training data we have, the more accurate our classifier can be. More data even always be better than having a fine tuned parameters.

Here's the en example of the corellation of dataset size and the accuracy of the classifier:

![More Data the Better](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/datasets_and_questions/slides/01_accuracy_vs_training_set_size.png)

## Data Types

Here are some types of data that we'll be dealing with:

* Numerical: numerical values (numbers) e.g. salary info.
* Categorical: limited number of discrete values (category) e.g. job title
* Time series: temporal value (date, timestamp) e.g. email timestamp
* Text: words e.g. email content, email recipients

## Exploring Enron Data

You can run the following command to explore some data from `enron_people.pkl` file:

```py
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python datasets_and_questions/explore_enron_data
```

You'll get the following output on the terminal:

```txt
🏢 Total number of people: 146
🌈 Total number of features: 21
🤡 Total people of interest: 18
💰 Total stock value for James Prentice: $1,095,040.00
💌 Total emails from Wesley Colwell to POI: 11
💰 Total amout of stock options excercised by Jeffrey K Skilling: $19,250,000.00
💰 Person with biggest payment: LAY KENNETH L ($103,559,793.00)
💵 People with salary information: 95
📧 People with email address information: 111
❓ People without total payment information: 21 (14.38%)
❓ POI without total payment information: 0 (0.00%)
```
As you might see all of the POI has a payment information available on the dataset.
