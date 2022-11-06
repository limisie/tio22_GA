from abc import ABC, abstractmethod
import numpy as np


class Fun(ABC):
    @abstractmethod
    def fun(self, x, y):
        pass

    @abstractmethod
    def derivative(self, x, y):
        pass

    def gradient(self, pred):
        return self.derivative(pred[0], pred[1])


class Himmelblau(Fun):
    def __init__(self):
        self.min = -5
        self.max = 5

    def fun(self, x, y):
        return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

    def derivative(self, x, y):
        dx = 2 * (2 * x * (x ** 2 + y - 11) + x + y ** 2 - 7)
        dy = 2 * (x ** 2 + 2 * y * (x + y ** 2 - 7) + y - 11)
        return np.asarray([dx, dy])


class Rastrigin(Fun):
    def __init__(self):
        self.min = -5.12
        self.max = 5.12

    def fun(self, x, y):
        return (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y)) + 20

    def derivative(self, x, y):
        dx = 2 * (x + 10 * np.pi * np.sin(2 * np.pi * x))
        dy = 2 * (y + 10 * np.pi * np.sin(2 * np.pi * y))
        return np.asarray([dx, dy])


class Matyas(Fun):
    def __init__(self):
        self.min = -10
        self.max = 10

    def fun(self, x, y):
        return 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y

    def derivative(self, x, y):
        dx = 0.52 * x - 0.48 * y
        dy = 0.52 * y - 0.48 * x
        return np.asarray([dx, dy])


class Rosenbrock(Fun):
    def __init__(self):
        self.min = -2
        self.max = 2

    def fun(self, x, y):
        return (x - 1) ** 2 + 10 * (y - x ** 2) ** 2

    def derivative(self, x, y):
        dx = 2 * (20 * x ** 3 - 20 * x * y + x - 1)
        dy = 20 * (y - x ** 2)
        return np.asarray([dx, dy])


class Beale(Fun):
    def __init__(self):
        self.min = -4.5
        self.max = 4.5

    def fun(self, x, y):
        return (1.5 - x - x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2

    def derivative(self, x, y):
        dx = 2 * x * (y ** 6 + y ** 4 - 2 * y ** 3 - y ** 2 + 2 * y + 3) + 5.25 * y ** 3 + 4.5 * y ** 2 - 3 * y - 12.75
        dy = 2 * x * (x * (3 * y ** 5 + 2 ** 3 - 3 * y ** 2 - y + 1) + 7.875 * y ** 2 + 4.5 * y - 1.5)
        return np.asarray([dx, dy])
