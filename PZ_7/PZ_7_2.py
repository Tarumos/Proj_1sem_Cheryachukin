# Вариант 29
# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку, расположенную
# между первым и вторым пробелом исходной строки. Если строка содержит только один пробел, то
# вывести пустую строку.
s = input()
a = s.split()  # сплитим и выводим результат
print(a[1] if len(a) > 2 else "")