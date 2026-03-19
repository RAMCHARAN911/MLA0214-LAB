import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# dataset
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,4,9,16,25])

# Linear Regression
lin_model = LinearRegression()
lin_model.fit(X, y)
lin_pred = lin_model.predict(X)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
poly_pred = poly_model.predict(X_poly)

print("Linear Regression Prediction:")
print(lin_pred)

print("Polynomial Regression Prediction:")
print(poly_pred)
