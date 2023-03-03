def right_triangle_cathets(cathet1, cathet2):
    """Функция ищет гипотенузу и площадь
     у катетов прямоугольного треугольника"""

    hypotenuse = (cathet1 ** 2 + cathet2 ** 2) ** 0.5
    area = (cathet1 * cathet2) / 2
    return f"Гипотенуза: {hypotenuse}\n"\
           f"Площадь: {area}"


print(right_triangle_cathets(3, 4))
# т.к. ты написал функцию, значит функция должна проверить корректность входных данных. Вот пример некорректного поведения программы:
print(right_triangle_cathets(-3, 2))
