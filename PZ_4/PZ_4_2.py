# Вариант 29.
# Даны положительные числа A, B, C. На прямоугольнике размера A x B размещено максимально возможное количество квадратов
# Со стороной C (без наложений). Найти количество квадратов, размещенных на прямоугольнике. Операции умножения и
# деления не использовать

a = input('Введите целое число!')  # ввод переменных
b = input('Введите целое число!')
c = input('Введите целое число!')
temp = int(input('Введите целое число!'))
K = 0
while type(a) != int:  # проверка на целочисленность
    try:
        a = int(a)
    except ValueError:
        print('Введите целое число')
        a = input()

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введите целое число')
        b = input()

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Введите целое число')
        c = input()

while a - c >= 0:
    a = a - c
    temp = b
    while temp - c >= 0:
        temp = temp - c
        K = K + 1

print(K)  # вывод результа
