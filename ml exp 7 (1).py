import math

X = [1, 2, 3, 4, 5, 6]
Y = [0, 0, 0, 1, 1, 1]

m = 0
c = 0
learning_rate = 0.1
epochs = 1000

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

for i in range(epochs):
    dm = 0
    dc = 0

    for x, y in zip(X, Y):
        z = m * x + c
        y_pred = sigmoid(z)

        dm += (y_pred - y) * x
        dc += (y_pred - y)

    m -= learning_rate * dm / len(X)
    c -= learning_rate * dc / len(X)

test_value = 4.5
probability = sigmoid(m * test_value + c)

print("Logistic Regression Algorithm")
print("-----------------------------")
print("Training Completed")
print("Slope value:", round(m, 4))
print("Intercept value:", round(c, 4))

print("\nTest Data: Hours Studied =", test_value)
print("Probability of Passing:", round(probability, 4))

if probability >= 0.5:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
