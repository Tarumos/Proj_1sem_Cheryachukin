default_radius = 5


def circle_perimeter(radius=default_radius):
    """
    Функция рассчитывает длину окружности

    Введите радиус или будет значение по умолчанию
    """
    return f'Длина окружности: {2 * 3.14 * radius}'


def circle_area(radius=default_radius):
    """
    Функция рассчитывает площадь окружности

    Введите радиус или будет значение по умолчанию
    """
    return f'Площадь окружности: {3.14 * radius * radius}'
