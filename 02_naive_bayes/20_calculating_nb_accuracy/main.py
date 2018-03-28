from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from terrain_data_generator import generateTerrainData

# Generate a random terrain data.
features_train, labels_train, features_test, labels_test = generateTerrainData()

# Create classifier.
classifier = GaussianNB()

# Train classifier.
classifier.fit(features_train, labels_train)

# Predict the output.
predicted_labels = classifier.predict(features_test)

# Calculating accuracy style 1 - with one liner filter.
total_corrects_1 = len([1 for i in range(0, len(predicted_labels)) if predicted_labels[i] == labels_test[i]])
accuracy_1 = total_corrects_1 / float(len(labels_test))
print("Accuracy 1: " + str(accuracy_1))

# Calculating accuracy style 2 - with basic loop.
total_corrects_2 = 0

for predicted_label, label_test in zip(predicted_labels, labels_test):
    if predicted_label == label_test:
        total_corrects_2 += 1

accuracy_2 = total_corrects_2 / float(len(labels_test))
print("Accuracy 2: " + str(accuracy_2))

# Calculating accuracy style 3 - with reduce function.
total_corrects_3 = reduce(lambda total, label: total + 1 if label[0] == label[1] else total, zip(predicted_labels, labels_test), 0)
accuracy_3 = total_corrects_3 / float(len(labels_test))
print("Accuracy 3: " + str(accuracy_3))

# Calculating accuracy style 4 - with sklearn accuracy_score.
accuracy_4 = accuracy_score(labels_test, predicted_labels)
print("Accuracy 4: " + str(accuracy_4))

# Calculating accuracy style 5 - use the score method.
accuracy_5 = classifier.score(features_test, labels_test)
print("Accuracy 5: " + str(accuracy_5))
