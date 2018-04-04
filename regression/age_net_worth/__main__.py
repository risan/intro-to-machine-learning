import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from data import get_data

# Get the absolute path to this directory.
dirname = os.path.dirname(os.path.realpath(__file__))

# Get the ages vs net worths data.
ages_train, ages_test, net_worths_train, net_worths_test = get_data()

# Create and train the linear regression.
regression = LinearRegression()
regression.fit(ages_train, net_worths_train)
net_worths_prediction = regression.predict(ages_test)

print("Net worth prediction for 28 years old person: ${0[0][0]:.2f}".format(regression.predict([[28]])))
print("⛰ Slope: {0[0][0]}".format(regression.coef_))
print("⤴️ Intercept: {0}".format(regression.intercept_))

coef_determination_train = regression.score(ages_train, net_worths_train)
print("📊 Coeficient of determination on training data: {0}".format(coef_determination_train))

coef_determination_test = regression.score(ages_test, net_worths_test)
print("📊 Coeficient of determination on test data: {0}".format(coef_determination_test))

# Plot the training data, test data and the prediction results.
plt.scatter(ages_train, net_worths_train, color = "b", label = "Train Data")
plt.scatter(ages_test, net_worths_test, color = "r", label = "Test Data")
plt.plot(ages_test, net_worths_prediction, color = "black")

plt.legend()
plt.xlabel("Ages")
plt.ylabel("Net Worths")
plt.savefig(os.path.join(dirname, "plot.png"))
plt.show()
