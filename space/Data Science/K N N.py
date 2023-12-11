import random
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
# print(iris.target)
# print(np.unique(iris.target, return_counts=True))
# print(iris.data.shape)
# print(iris.data)
# print(iris.target)
delta = np.sum((iris.data - iris.data[1]) ** 2, axis=1) ** 0.5


# print(iris.data.shape)


# print(delta)
# print('a')
# pos_sort = np.argsort(delta)
# pos_sort_5 = pos_sort[:5]
# print(pos_sort_5)
# print(iris.target[pos_sort_5])


# print(iris.data[[1, 34, 45, 12, 9, 25, 30, 35, 2, 49, 3, 29, 47, 7, 39, 11, 28, 26,
#                  38, 8, 6, 40, 0, 17, 42, 23, 27, 4, 37, 24, 31, 43, 13, 20, 21, 22,
#                  36, 48, 41, 19, 46, 10, 44, 16, 5, 32, 18, 33, 14, 15, 98, 57, 93, 79,
#                  60, 64, 81, 80, 69, 59, 82, 89, 92, 53, 67, 88, 99, 62, 71, 95, 94, 96,
#                  90, 61, 97, 55, 84, 66, 74, 106, 78, 87, 85, 91, 75, 73, 51, 68, 65, 63,
#                  58, 54, 56, 70, 138, 86, 126, 121, 72, 127, 119, 76, 50, 123, 83, 113, 149, 133,
#                  101, 142, 52, 146, 77, 114, 110, 147, 111, 134, 137, 115, 116, 145, 141, 103, 148, 128,
#                  139, 132, 112, 136, 108, 124, 140, 104, 129, 120, 144, 143, 100, 102, 125, 130, 107, 109,
#                  135, 131, 105, 122, 117, 118]])


def distance_between_flowers(array_of_information, array_target, single_value):
    array_delta = np.sum((array_of_information - single_value) ** 2, axis=1) ** 0.5
    array_pos_sort = np.argsort(array_delta)
    pos_sort_5 = array_pos_sort[:5]
    return np.bincount(array_target[pos_sort_5]).argmax()


def randomly_divide(x, y):
    """Randomly divides an array into 80, 20 percent"""
    size = x.shape[0]

    random_array = np.random.permutation(np.arange(size))
    x_train = x[random_array[:int(size // 1.25)]]
    y_train = y[random_array[:int(size // 1.25)]]
    x_test = x[random_array[int(size // 1.25):]]
    y_test = y[random_array[int(size // 1.25):]]

    return x_train, y_train, x_test, y_test


def find_lebel(x_train, y_train, x_test, y_test):
    count = 0
    for i, vector in enumerate(x_test):
        if distance_between_flowers(x_train, y_train, vector) == y_test[i]:
            count += 1
    return count / y_test.shape[0], count


# print(distance_between_flowers(iris.data, iris.target, iris.data[130]))

x_train, y_train, x_test, y_test = randomly_divide(iris.data, iris.target)
print(find_lebel(x_train, y_train, x_test, y_test))
# print(distance_between_flowers(x_train, y_train, x_test[1]))
print(np.bincount([1, 2, 2, 1, 0]).argmax())
