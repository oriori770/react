def calculate_gradient(func, x, epsilon=1e-6):
    """
    Calculate the gradient of a function at a specific point using numerical differentiation.

    Parameters:
    - func: The function for which the gradient is calculated.
    - x: The point at which the gradient is computed.
    - epsilon: The small value used for numerical differentiation (default is 1e-6).

    Returns:
    - The gradient of the function at the specified point.
    """
    # Calculate the gradient using numerical differentiation (central difference)
    gradient = (func(x + epsilon) - func(x - epsilon)) / (2 * epsilon)

    return gradient


def gradient_descent(func, initial_x, learning_rate=0.1, num_iterations=50):
    """
    Perform gradient descent to find the minimum point of a function.

    Parameters:
    - func: The function for which the minimum point is sought.
    - initial_x: The starting point for the optimization.
    - learning_rate: The step size for each iteration (default is 0.1).
    - num_iterations: The number of iterations for the optimization (default is 100).

    Returns:
    - The minimum point found by the gradient descent algorithm.
    """
    x = initial_x

    for iteration in range(num_iterations):
        gradient = calculate_gradient(func, x)
        x = x - learning_rate * gradient
        print(x)

    return x


# Example function: f(x) = x^2
def example_function(x):
    return x ** 2 - 56 * x + x * 0.5


# Initial guess
initial_guess = 900

# Apply gradient descent to find the minimum of the example function
minimum_point = gradient_descent(example_function, initial_guess)

# Print the result
print(f"The minimum point found by gradient descent is: {minimum_point}")
print(0 < minimum_point < 0.1)
