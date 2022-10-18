# Вариант 29.
# 2. На числовой оси расположены три точки: A,B,C. Определить, какая из двух
# последних точек (B или C) расположена ближе к A, и вывести эту точку и ее
# расстояние от точки A.
a = input()
b = input()
c = input()

while type(a) != int:
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

ac = abs(a - c)
ab = abs(a - b)

if ac < ab:
    print('a ближе')
if ab < ac:
    print('b ближе')
if ab == ac:
    print('расстояние одинаково')
