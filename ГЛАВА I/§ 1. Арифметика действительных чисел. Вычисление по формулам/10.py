import math

h1 = int(input())


def time_of_the_fall_of_stone(h, g):
    """ Функция определяет время падения камня на поверхность земли с высоты h """

    time = math.sqrt(2 * h / g)
    return f"Время, необходимое камню для падения с высоты {h} метров {time} секунд"


print(time_of_the_fall_of_stone(h1, g=9.81))
# Некорректные решения: 
print(time_of_the_fall_of_stone(-2, g=9.81))
print(time_of_the_fall_of_stone(10000, 0))

