def resistances(r1, r2, r3):
    """ Функция находит сопротивление параллельного соединения"""
    R = 1 / (1 / r1 + 1 / r2 + 1 / r3)
    return f'Эквивалентное сопротивление: {R}'


print(resistances(1, 2, 3))
# Некорректные решения: 
print(resistances(0, 2, 3))
print(resistances(1, 0, 3))
print(resistances(1, 2, 0))
print(resistances(1, -2, 3))




