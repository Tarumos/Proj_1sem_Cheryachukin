from random import randint

a = [randint(-10, 10) for i in range(randint(2, 10))]
b = [x for x in a if x % 2 == 0 and x > 0]
print(f'Первоначальный список: {a}\n'
      f'Список четных положительных элементов: {b}\n'
      f'Сумма 2-го списка: {sum(b)}\n'
      f'Среднее арифметическое 2-го списка: {sum(b) / len(b)}')
