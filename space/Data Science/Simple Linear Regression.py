from typing import List
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


Vector = List[float]

x = [i for i in range(-100, 110, 10)]
y = [3 * i - 5 for i in x]

fig = plt.figure(figsize=(10, 5))
plt.plot(x, y)

# Show the plot
plt.show()
# plt.bar(x, y)
# plt.show()


# print(x, y)


def predict(alpha: float, beta: float, x_i: float) -> float:
    return beta * x_i + alpha


def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """
    The error from predicting beta * x_i + alpha
    when the actual value is y_i
    """
    return predict(alpha, beta, x_i) - y_i


def sum_of_sqerrors(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x, y))
