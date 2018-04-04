# Regressions

## Table of Contents

* [Regression Summary](#regression-summary)
* [Age vs Net Worth](#age-vs-net-worth)
* [Age vs Net Worth with Scikit Learn](#age-vs-net-worth-with-scikit-learn)
    * [Create and Train Linear Regression](#create-and-train-linear-regression)
    * [Run the Classifier](#run-the-classifier)
    * [Age vs Net Worth Result](#age-vs-net-worth-result)

## Regression Summary

* Continous supervised learning means the output is continues—the output is no longer a discrete values.
* Discrete output can be like: fast/slow, flat/bumpy, email's authors.
* Continouse output can be like: vehicle speed, income, age in unix seconds—there's some sense of ordering.

## Age vs Net Worth

* Suppose we have the age vs net worths data. The age is the input on the x-axis, while the net worth is the output on the y-axis.
* We know that net worth is a continous output because there's some sense of odering—there's not much of a difference between $100 and $99.

![Age vs Net Worth](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/regression/slides/01_age_vs_net_worth.png)

* We can solve this using regression (the green line). The line equation can be formulatted:

```
net_worths = 6.25 * age + 0
```

* `6.25` is the **slope**. The bigger it's, the more steep our line become.
* `0` is the **intercept**. It's the starting point for the y-axis.

![Slope vs Intercept](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/regression/slides/02_slope_and_intercept.png)

* Knowing this line equation, we can now predict the net worth for anyone within the range of age 0 - 80 years.

![Prediction with Regression](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/regression/slides/03_prediction_with_regression.png)

## Age vs Net Worth with Scikit Learn

### Create and Train Linear Regression

With scikit learn we can easily create a [linear regression model](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression):

```py
from sklearn.linear_model import LinearRegression

# Create the linear regression.
regression = LinearRegression()

# Train the linear regression.
regression.fit(ages_train, net_worths_train)

# Predict the data.
net_worths_prediction = regression.predict(ages_test)
```

### Run the Classifier

Type the following command on your terminal to run the age vs net worth regression:

```shell
# Go to the project directory.
$ cd /path/to/intro-to-machine-learning

# And run it with Python
$ python regression/age_net_worth
```

### Age vs Net Worth Result

You should get the following plot. The black line is the net worth prediction for te given test point.

```txt
⛰ Slope: 6.47354954955
⤴️ Intercept: [-14.35378331]
📊 Coeficient of determination on training data: 0.874588235823
📊 Coeficient of determination on test data: 0.812365729232
```

![Age vs Net Worth Result](https://raw.githubusercontent.com/risan/intro-to-machine-learning/master/regression/age_net_worth/plot.png)
