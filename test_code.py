from math import sqrt

message = """Добро пожаловать в самую лучшую программу для вычисления
квадратного корня из заданного числ
"""
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Программа для вычесления корня."""
    if your_number <= 0:
        return
    print(
        f'Мы вычислили квадратный корень '
        f'из введённого вами числа. '
        f'Это будет: {calculate_square_root(your_number)}')


print(message)
calc(25.5)
