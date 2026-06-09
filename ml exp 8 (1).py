
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)

sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(xi * xi for xi in x)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
c = (sum_y - m * sum_x) / n

print("Linear Regression Equation:")
print("y =", round(m, 2), "x +", round(c, 2))

x_test = 6
y_pred = m * x_test + c

print("\nFor x =", x_test)
print("Predicted y =", round(y_pred, 2))
