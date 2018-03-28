# Calculating Naive Bayes Accuracy

To calculate the accuracy of our classifier, we simply count the total number of test records that are correctly preddicted then divide it by the total number of test records. There are many ways to do this.

### 1 With One Liner Array Filter

One of the way is by filtering the `predicted_labels` records that matched the actual `labels_test`.

```py
total_corrects = len([1 for i in range(0, len(predicted_labels)) if predicted_labels[i] == labels_test[i]])
accuracy_1 = total_corrects / float(len(labels_test))
print("Accuracy: " + str(accuracy))
```

Note that in order to have a `float` number as the division result, we need to cast the divider to `float`.

### 2 With Basic For..In Loop

```py
total_corrects = 0

for predicted_label, label_test in zip(predicted_labels, labels_test):
    if predicted_label == label_test:
        total_corrects += 1

accuracy = total_corrects / float(len(labels_test))
print("Accuracy: " + str(accuracy))
```

### 3 With Reduce Function

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

### 4 With accuracy_score

One of the easiest way is to use the built-int `accuracy_score` function from scikit-learn. The first argument is the real output values, the second one if the predicted outputs.

```py
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, predicted_labels)
print("Accuracy: " + str(accuracy))
```

### 5 With score Method

Most of the classifier from scikit-learn has the `score` method to calculate the accuracy, so we can use this instead of importing `accuracy_score`. The first parameter is the input features and the second parameter is the true output values.

```py
accuracy = classifier.score(features_test, labels_test)
print("Accuracy: " + str(accuracy))
```
