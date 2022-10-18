N = input()  # Ввод числа

while type(N) != int:  # Проверка на целочисленность
    try:
        N = int(N)
    except ValueError:
        print()
        N = input

result = 1  # Задаем переменные
K = 1.2

if N > 0:  # Находим произведение
    while N != 1:
        result = result * K
        K = K + 0.1
        N = N - 1
