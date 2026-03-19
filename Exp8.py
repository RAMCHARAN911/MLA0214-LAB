# Linear Regression example

from sklearn.linear_model import LinearRegression
import numpy as np

# training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# create model
model = LinearRegression()

# train model
model.fit(X, y)

# prediction
x_test = np.array([[6]])
y_pred = model.predict(x_test)

print("Predicted value for 6:", y_pred)
