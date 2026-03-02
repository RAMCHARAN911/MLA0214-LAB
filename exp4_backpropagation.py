import numpy as np

# XOR dataset
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],[1],[1],[0]])

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights randomly
np.random.seed(1)
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))
wo = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bo = np.random.uniform(size=(1, output_neurons))

learning_rate = 0.1

# Training
for i in range(5000):
    
    # Forward Propagation
    hidden_input = np.dot(X, wh) + bh
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, wo) + bo
    predicted_output = sigmoid(final_input)
    
    # Backpropagation
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    
    error_hidden = d_predicted_output.dot(wo.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)
    
    # Update weights
    wo += hidden_output.T.dot(d_predicted_output) * learning_rate
    wh += X.T.dot(d_hidden) * learning_rate

print("\nPredicted Output after Training:")
print(predicted_output)
