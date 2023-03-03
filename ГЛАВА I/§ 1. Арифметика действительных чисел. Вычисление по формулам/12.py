side_input = int(input())


def area_triangle(side1):
    """ Функция находит площфдь равностороннего треугольника """
    area = (1.73 * side1 * side1) / 4
    return f"Площадь равностороннего треугольника равна: {area}"


print(area_triangle(side_input))
