import numpy as np

# Setting up the data
# x: input data
# y: labels for the data
# each row in x is a chord and each row in y is the sound associated with that chord

x = np.array([[0, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [1, 1, 1]])

y = np.array([[1],
              [-1],
              [1],
              [-1]])

# Setting up the neural network
# Input layer
input_layer_size = x.shape[1]

# Hidden layer
hidden_layer_size = 2

# Weights between input and hidden layer
W1 = np.random.randn(input_layer_size, hidden_layer_size)

# Weights between hidden and output layer
W2 = np.random.randn(hidden_layer_size, 1)

# Learning rate
learning_rate = 0.1

# Training the network
for epoch in range(10000):
    # Forward Propagation
    z1 = np.dot(x, W1)
    a1 = np.tanh(z1)
    z2 = np.dot(a1, W2)
    a2 = np.tanh(z2)

    # Calculating the error
    error = a2 - y

    # Backpropagation
    delta2 = error * (1 - a2 ** 2)
    delta1 = delta2.dot(W2.T) * (1 - a1 ** 2)

    # Updating weights
    W2 = W2 - learning_rate * a1.T.dot(delta2)
    W1 = W1 - learning_rate * x.T.dot(delta1)

# Make predictions
predictions = np.tanh(np.dot(np.tanh(np.dot(x, W1)), W2))

print(predictions)
