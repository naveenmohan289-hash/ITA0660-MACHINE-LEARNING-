
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

print("Linear Regression")
n = len(x)

sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(i * i for i in x)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
c = (sum_y - m * sum_x) / n

print("Equation: y =", round(m, 2), "x +", round(c, 2))

print("\nPredicted Values:")
for i in x:
    print("x =", i, "y =", round(m * i + c, 2))

print("\nPolynomial Regression")
print("Equation: y = x^2")

print("\nPredicted Values:")
for i in x:
    print("x =", i, "y =", i * i)

print("\nComparison:")
print("Linear Regression fits a straight line.")
print("Polynomial Regression fits a curved line.")
print("Polynomial Regression is better for nonlinear data.")
