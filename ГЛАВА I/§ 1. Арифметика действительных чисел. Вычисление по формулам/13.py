line = int(input())


def period_oscillation(l, g):  # g = Ускорение силы тяжести
    """ Функция вычесляет период колебания маятника длины l """

    Period = 2 * (l / g)
    return f"Период колебаний: {Period}"


print(period_oscillation(line, g=9.8))
