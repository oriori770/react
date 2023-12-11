# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Creating vectors X and Y
x = np.linspace(-2, 2, 100)
y = x ** 2

fig = plt.figure(figsize=(10, 5))
# Create the plot
# plt.plot(x, y)

# Show the plot
# plt.show()


def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def binomial_distribution(p, n):
    y = []
    x = []
    for k in range(n + 1):
        x.append(k)
        y.append(binomial_coefficient(n, k) * (p ** k) * (1 - p) ** (n - k))
    plt.bar(x, y)
    plt.show()

# a = (1,2)
binomial_distribution(0.7, 100)