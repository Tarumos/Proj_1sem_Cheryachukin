# Вариант 29. Дни недели пронумерованны следующим образом: 0 - воскресенье, 1 - понедельник, ..., 6 - суббота.
# Дано целое число K, лежащее в диапозоне 1-365. Определить номер дня недели для K-го дня года, если известно, что
# в этом году 1 января было понедельником.
result = 0
K = input('Введите число от 1 до 365!')  # ввод числа
while type(K) != int:
    try:
        K = int(K)  # попытка привести K к int
    except ValueError:
        print('Введите целое число')
        K = input()

first_day_month = 1  # назначаем переменную
num = K % 7  # ищем остаток от деления
result = (((first_day_month - 1) + num) % 7)  # считает результат
print(result)  # Выводим результат