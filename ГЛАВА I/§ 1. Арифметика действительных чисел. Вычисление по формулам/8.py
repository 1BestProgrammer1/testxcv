import math


def perimeter(n, r):
    """ Функция определяет периметр правильного n-угольника,
        описанногооколо окружности радиуса r. """
    total = 2 * n * r * math.sin(math.pi / n)
    return total


perimeter_1 = perimeter(6, 2)
print("Периметр многоугольника =", perimeter_1)
