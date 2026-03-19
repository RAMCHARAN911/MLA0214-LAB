# Logistic Regression example

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# load dataset
data = load_iris()
X = data.data
y = data.target

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# create model
model = LogisticRegression(max_iter=200)

# train model
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# accuracy
acc = accuracy_score(y_test, y_pred)

print("Predicted Values:", y_pred)
print("Accuracy:", acc)
