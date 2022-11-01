# Вариант 29
# Составить функцию, которая напечатает сорок любых символов.
# Описать функцию Swap(Х, У), меняющую содержимое переменных X и Y (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# ее помощью для данных переменных A, B, C, D последовательно поменять
# содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C, D.

def Swap(zxc):  # описываем функцию меняющую содержимое переменных
    zxc[0], zxc[1] = zxc[1], zxc[0]
    return zxc


A = input('Введите число!')
B = input('Введите число!')
C = input('Введите число!')
D = input('Введите число!')
print("A = ", A)  # Выводим результаты
print("B = ", B)
print("C = ", C)
print("D = ", D)
print()

A1 = A
B1 = B
C1 = C
D1 = D

A, B = B, A  # свапаем
C, D = D, C
B, C = C, B

print("A = ", A)  # Выводим результаты
print("B = ", B)
print("C = ", C)
print("D = ", D)
print()

zxc = [A1, B1]
A1, B1 = Swap(zxc)
zxc = [C1, D1]
C1, D1 = Swap(zxc)
zxc = [B1, C1]
B1, C1 = Swap(zxc)
print("A = ", A1)  # Выводим результаты
print("B = ", B1)
print("C = ", C1)
print("D = ", D1)
