# Naive Bayes

Naive Bayes is one of the supervised learning algorithm. The Naive Bayes classifier uses the Bayes' Theorem with  assumption that each feature is independence from one and antoher—that's why it's called naive.

## Table of Contents

* [Bayes Rules](#bayes-rules)
    * [The Cancer Case](#the-cancer-case)
        * [Prior Probability](#prior-probability)
        * [The Test Evidence](#the-test-evidence)
        * [The Posterior Probability](#the-posterior-probability)
        * [Normalizing](#normalizing)
    * [Text Learning](#text-learning)
        * [Who Sent Love Life](#who-sent-love-life)
        * [Who Sent Life Deal](#who-sent-life-deal)
        * [Who Sent Love Deal](#who-sent-love-deal)
* [Naive Bayes Strengths and Weeknesses](#naive-bayes-strengths-and-weeknesses)
* [Terrain Classifier with Naive Bayes](#terrain-classifier-with-naive-bayes)
    * [Create and Train a Gaussian Naive Bayes Classifier](#create-and-train-a-gaussian-naive-bayes-classifier)
    * [Run the Classifier](#run-the-classifier)
    * [Terrain Classifier Result](#terrain-classifier-result)
* [Calculating Classifier Accuracy](#calculating-classifier-accuracy)
    * [With One Liner List Filter](#with-one-liner-list-filter)
    * [With Basic For..In Loop](#with-basic-forin-loop)
    * [With Reduce Function](#with-reduce-function)
    * [Using accuracy_score](#using-accuracy_score)
    * [Using score Method](#using-score-method)
* [Email Classifier with Naive Bayes](#email-classifier-with-naive-bayes)

## Bayes Rules

### The Cancer Case

#### Prior Probability

Let say in the entire population, the probability to get a cancer is 1%. This is called the **prior probability**.

```txt
P(C) = 0.01
```

#### The Test Evidence

There are two branches of events here: **WITH CANCER** and **WITHOUT CANCER**. And suppose there's a cancer test that can be conducted with two possible results: **POSITIVE** and **NEGATIVE**.

Given a person **with cancer**, he/she has the probability of 90% to get a **positive** cancer test result. This is also called the **test sensitivity**:

```txt
P(pos|C) = 0.9

# Thus
P(neg|C) = 0.1
```

Given a person **without cancer**, he/she has the probability of 90% to get a **negative** cancer test result. This is called the **test specitivity**:

```txt
P(neg|Cnot) = 0.9

# Thus
P(pos|Cnot) = 0.1
```

#### The Posterior Probability

Now the question is, what is the probability of people to get a cancer given a positive test result?

To arrive at **posterior probability**, we need both the prior probability and the test evidence.

```
Prior Probability x Test Evidence => Posterior Probability
```

First we need to calculate the joint probability of two events (with & without cancer) given the positive test result.

```txt
# Joint probability of getting cancer given positive result.
P(C|pos) = P(C) * P(pos|C)
         = 0.01 * 0.9
         = 0.009

# Joint probability of not getting cancer given positive result.
P(Cnot|pos) = P(Cnot) * P(pos|Cnot)
            = 0.99 * 0.1
            = 0.099
```

#### Normalizing

We can combine the above two equations to get the normalizer value.

```txt
P(pos) = P(C|pos) + P(Cnot|pos)
       = 0.009 + 0.099
       = 0.108
```

We can then use this normalizer value to get the posterior probabilty by using it as a divider.

```txt
# Posterior probability of getting cancer given positive result.
P(C|pos) = Joint P(C|pos) / normalizer
         = 0.009 / 0.108
         = 0.083

# Posterior probability of not getting cancer given positive result.
P(Cnot|pos) = Joint P(Cnot|pos) / normalizer
            = 0.099 / 0.108
            = 0.917
```

Note that the total of probability is `1`!

### Text Learning

Suppose we have these two people: **Chris** and **Sarah**. We gather their emails and count the frequencies of the words: **Love**, **Deal**, and **Life**. Based on how frequent they use these words, we now have the following possibilities:

```txt
      | LOVE | DEAL | LIFE |
CHRIS |  0.1 |  0.8 |  0.1 |
SARAH |  0.5 |  0.2 |  0.3 |
```

And both have the same amount of prior probability to send email:

```txt
P(C) = 0.5
P(S) = 0.5
```

#### Who Sent Love Life

Now the first, question, who sent the email with `Love Life` text?

```txt
P(C|love life) = P(C) * P(love|C) * P(life|C)
               = 0.5 * 0.1 * 0.1
               = 0.005

P(S|love life) = P(S) * P(love|S) * P(life|S)
               = 0.5 * 0.5 * 0.3
               = 0.0375
```

It was **Sarah**!

#### Who Sent Life Deal

Next, who sent the email with `Life Deal` text?

```txt
P(C|life deal) = P(C) * P(life|C) * P(deal|C)
               = 0.5 * 0.1 * 0.8
               = 0.04

P(S|life deal) = P(S) * P(life|S) * P(deal|S)
               = 0.5 * 0.3 * 0.2
               = 0.03
```

It was **Chris**! Now let's try to calculate the prior probability of these words both for Chris and Sarah.

```txt
# Calculate the normalizer
P(life deal) = P(C|life deal) + P(S|life deal)
             = 0.04 + 0.03
             = 0.07

# Prior probability of Chris given "life deal"
P(C|life deal) = Joint P(C|life deal) / normalizer
               = 0.04 / 0.07
               = 0.57

# Prior probability of Sarah given "life deal"
P(S|life deal) = Joint P(S|life deal) / normalizer
               = 0.03 / 0.07
               = 0.43
```

#### Who Sent Love Deal

Next, we're going to calculate the prior probability of Chris and Sarah given the text is `Love Deal`.

```txt
# Joint probability of Chris given "love deal"
P(C|love deal) = P(C) * P(love|C) * P(deal|C)
               = 0.5 * 0.1 * 0.8
               = 0.04

# Joint probability of Sarah given "love deal"
P(S|love deal) = P(S) * P(love|S) * P(deal|S)
               = 0.5 * 0.5 * 0.2
               = 0.05

# Calculate the normalizer
P(love deal) = P(C|love deal) + P(S|love deal)
             = 0.04 + 0.05
             = 0.09

# Prior probability of Chris given "love deal"
P(C|love deal) = Joint P(C|love deal) / normalizer
               = 0.04 / 0.09
               = 0.444

# Prior probability of Sarah given "love deal"
P(S|love deal) = Joint P(S|love deal) / normalizer
               = 0.05 / 0.09
               = 0.556
```

## Naive Bayes Strengths and Weeknesses

Naive Bayes is simple to use and efficient. We can feed it with thousands even hundred thousands of features.

Naive Bayes is a very good for text classification. When dealing with text, it's very common to treat each word as a feature; thus we'll ended up with bunch of features—and Naive Bayes really efficient in handling a big set of features.

However it can break in a funny way. Historically when Google first started out, people searched for "Chicago Bulls" would ended up getting an image of bulls and Chicago city. Naive Bayes does not consider the word order, thus can't handle phrases with multiple words and totally have different meaning.

> It's called "Naive" because it simply calculate the word frequencies without considering the word order.

## Terrain Classifier with Naive Bayes

### Create and Train a Gaussian Naive Bayes Classifier

With scikit-learn we can easily create and train a [Gaussian Naive Bayes classifier](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html):

```py
from sklearn.naive_bayes import GaussianNB

# Create the classifier instance.
classifier = GaussianNB()

# Train the classifier.
classifier.fit(features_train, labels_train)

# Predict the output labels.
clasifier.predict(features_test)
```
Read more in [GaussianNB documentation](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html).

### Run the Classifier

Type the following command on your terminal to run the terrain classifier:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python naive_bayes/terrain_classifier
```

### Terrain Classifier Result

The result from using the Gaussian Naive Bayes classifier to predict the vehicle's speed given a terrain condition.

```txt
🤖 Accuracy: 0.884
```

![Gaussian Naive Bayes decision boundary](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/naive_bayes/terrain_classifier/plot.png)

## Calculating Classifier Accuracy

To calculate the accuracy of our classifier, we simply count the total number of test records that are correctly preddicted then divide it by the total number of test records. There are many ways to do this.

### With One Liner List Filter

One of the way is by filtering the `predicted_labels` records that matched the actual `labels_test`.

```py
total_corrects = len([1 for i in range(0, len(predicted_labels)) if predicted_labels[i] == labels_test[i]])
accuracy = total_corrects / float(len(labels_test))
print("Accuracy: " + str(accuracy))
```

Note that in order to have a `float` number as the division result, we need to cast the divider to `float`.

### With Basic For..In Loop

```py
total_corrects = 0

for predicted_label, label_test in zip(predicted_labels, labels_test):
    if predicted_label == label_test:
        total_corrects += 1

accuracy = total_corrects / float(len(labels_test))
print("Accuracy: " + str(accuracy))
```

### With Reduce Function

The other way to count the matched records is through the `reduce` function:

```py
total_corrects = reduce(lambda total, label: total + 1 if label[0] == label[1] else total, zip(predicted_labels, labels_test), 0)
accuracy = total_corrects / float(len(labels_test))
print("Accuracy: " + str(accuracy))
```

We can break this down to four parts:

- `carry`: It's the carried value from the previous round.
- `item`: It's the list item that currently being passed.
- `the_next_cary_value`: This is statement that will be the next `carry` value.
- `items`: The list of items to reduce.
- `initialCarryValue`: It's the optional argument, and it will be the initial value for the `carry`.

```py
reduce(lambda carry, item: the_next_cary_value, items, [initialCarryValue])
```

### Using accuracy_score

One of the easiest way is to use the built-int `accuracy_score` function from scikit-learn. The first argument is the real output values, the second one if the predicted outputs.

```py
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, predicted_labels)
print("Accuracy: " + str(accuracy))
```

### Using score Method

Most of the classifier from scikit-learn has the `score` method to calculate the accuracy, so we can use this instead of importing `accuracy_score`. The first parameter is the input features and the second parameter is the true output values.

```py
accuracy = classifier.score(features_test, labels_test)
print("Accuracy: " + str(accuracy))
```

## Email Classifier with Naive Bayes

Type the following command on your terminal to run the email classifier:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python naive_bayes/email_classifier
```

The result of using Gaussian Naive Bayes classifier to predict the email's author:

```txt
⏱ Training time: 1.951s
⏱ Predicting time: 0.173s
🤖 Accuracy: 0.9732650739476678

👦 Total emails from Chris: 906
👧 Total emails from Sarah: 852
```
