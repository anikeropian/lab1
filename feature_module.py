def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b


def divide(a, b):
    """Возвращает частное двух чисел."""
    if b == 0:
        raise ValueError('Деление на ноль невозможно')
    return a / b