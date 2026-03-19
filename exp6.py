# Naive Bayes implementation

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# load dataset
data = load_iris()
X = data.data
y = data.target

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# create model
model = GaussianNB()

# train model
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# confusion matrix
cm = confusion_matrix(y_test, y_pred)

# accuracy
acc = accuracy_score(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

print("Accuracy:", acc)
