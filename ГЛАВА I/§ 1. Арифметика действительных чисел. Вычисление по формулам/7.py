def right_triangle_cathets(v1,  v2, t1, t2):
    """Функция ищет объем и температуру образовавшейся смеси"""

    v_mixture = v1 + v2
    t_mixture = (v1 * t1 + v2 * t2) / v_mixture
    
    return f"Объем смеси составляет: {v_mixture} литров\n" \
           f"Температура смеси составляет: {t_mixture}"


print(right_triangle_cathets(3, 3, 4, 4))
# Некорректные решения: 
print(right_triangle_cathets(3, -3, 4, 4))
print(right_triangle_cathets(3000, 3000, 50, 4)) # 3000 - пользователь ввел миллилитры
