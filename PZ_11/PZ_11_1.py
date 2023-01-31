from random import randint
f1 = open('1.txt', 'w', encoding='UTF-8')
f1.write(', '.join(str(randint(-10, 10)) for _ in range(5, 10)))
f1.close()

f2 = open('2.txt', 'w', encoding='UTF-8')
f2.write(', '.join(str(randint(-10, 10)) for _ in range(5, 10)))
f2.close()

f1 = open('1.txt', 'r', encoding='UTF-8')
a = f1.readline().split(', ')
f1.close()

f2 = open('2.txt', 'r', encoding='UTF-8')
b = f2.readline().split(', ')
f2.close()

c = 0
q = 0

for i in a:
    if int(i) % 2 == 0:
        c += 1

for i in b:
    if int(i) % 2 == 1:
        q += 1

f3 = open('result.txt', 'w', encoding='UTF-8')
f3.writelines(['Элементы первого и второго файлов ' + ", ".join(a + b),
               f"\nКоличество элементов первого и второго файлов {len(a) + len(b)}",
               f"\nКоличество элементов, общих для двух файлов {len(set(a) & set(b))}",
               f"\nКоличество четных элементов первого файла {c}",
               f"\nКоличество нечетных элементов второго файла {q}"])
