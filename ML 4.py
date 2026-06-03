import numpy as np

# -----------------------------
# 1. DATASET (XOR)
# -----------------------------
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],[1],[1],[0]])

# -----------------------------
# 2. ACTIVATION FUNCTION
# -----------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# -----------------------------
# 3. INITIALIZE WEIGHTS
# -----------------------------
np.random.seed(1)

input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# weights
W1 = np.random.uniform(size=(input_neurons, hidden_neurons))
W2 = np.random.uniform(size=(hidden_neurons, output_neurons))

# biases
b1 = np.random.uniform(size=(1, hidden_neurons))
b2 = np.random.uniform(size=(1, output_neurons))

# -----------------------------
# 4. TRAINING (BACKPROPAGATION)
# -----------------------------
epochs = 10000
learning_rate = 0.1

for i in range(epochs):

    # Forward Propagation
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)

    # Error
    error = y - predicted_output

    # Backpropagation
    d_output = error * sigmoid_derivative(predicted_output)

    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights & biases
    W2 += hidden_output.T.dot(d_output) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate

    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# -----------------------------
# 5. TEST OUTPUT
# -----------------------------
print("Final Output after Training:\n")
print(predicted_output)

# -----------------------------
# 6. TEST NEW SAMPLE
# -----------------------------
def predict(x):
    h = sigmoid(np.dot(x, W1) + b1)
    o = sigmoid(np.dot(h, W2) + b2)
    return np.round(o)

print("\nPredictions:")
for sample in X:
    print(sample, "->", predict(sample.reshape(1, -1))[0][0])
