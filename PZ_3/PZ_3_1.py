# Вариант 29.
# 1. Даны числа x, y,x1, y1, x2, y2. Проверить истинность высказывания: "Точка с
# координатами (x, y) лежит внутри прямоугольника, левая вершина которого
# имеет координаты (x1, y1), правая нижняя - (x2, y2), а стороны параллельны
# координатым осям".

x = input()  # Ввод числа
y = input()
x1 = input()
y1 = input()
x2 = input()
y2 = input()
while type(x) != int:  # Проверка на целочисленность
    try:
        x = int(x)
    except ValueError:
        print('Введите целое число')
        x = input()
while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print('Введите целое число')
        y = input()
while type(x1) != int:
    try:
        x1 = int(x1)
    except ValueError:
        print('Введите целое число')
        x1 = input()
while type(y1) != int:
    try:
        y1 = int(y1)
    except ValueError:
        print('Введите целое число')
        y1 = input()
while type(x2) != int:
    try:
        x2 = int(x2)
    except ValueError:
        print('Введите целое число')
        x2 = input()
while type(y2) != int:
    try:
        y2 = int(y2)
    except ValueError:
        print('Введите целое число')
        y2 = input()
if (x1 < x < x2) and (y1 > y > y2):  # Я думаю тут все логично
    print('Водит в прямоугольник')  # Вывод результата
else:
    print('Ну входит в прямоугольник')
