# Expectation Maximization using Gaussian Mixture Model

import numpy as np
from sklearn.mixture import GaussianMixture

# sample data
X = np.array([[1], [2], [3], [10], [11], [12]])

# create EM model
model = GaussianMixture(n_components=2)

# train model
model.fit(X)

# predict clusters
labels = model.predict(X)

print("Data points:", X.flatten())
print("Cluster labels:", labels)
