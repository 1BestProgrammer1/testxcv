side_input = int(input())

SQRT_THREE = 3 ** 0.5


def area_triangle(side1):
    """ Функция находит площфдь равностороннего треугольника """
    area = (1.73 * side1 * side1) / 4
    # А если мне нужна точность выше 2 знаков?
    # Всегда стоит оставлять расчет корней и тригонометрии  в том виде, которые записан в формуле.
    # Плохой вариант, вычислять константное значение каждый раз, когда вызывается функция.
    # В этом случае, стоит вынести расчет выше функции в отдельную константу.  
    # В Питоне нельяз создать неизменяемую переменную, но есть соглашение такие константы писать большими буквами
    area = (SQRT_THREE * side1 * side1) / 4
    return f"Площадь равностороннего треугольника равна: {area}"


print(area_triangle(side_input))
