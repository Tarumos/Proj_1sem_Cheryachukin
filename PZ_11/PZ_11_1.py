from random import randint

with open("first.txt", "w") as first:
    f_li = [randint(-10, 10) for _ in range(10)]
    first.write(f"{f_li}")

with open("second.txt", "w") as second:
    s_li = [randint(-10, 10) for _ in range(10)]
    second.write(f"{s_li}")

with open("answer.txt", "w") as answer:
    lists = f_li + s_li
    answer.writelines([
        f"Элементы первого и второго файлов: {lists} \n",
        f"Количество элементов первого и второго файлов: {len(lists)} \n",
        f"Количество элементов, общих для двух файлов: {len(set(f_li) & set(s_li))} \n",
        f"Количество четных элементов первого файла: {list(filter(lambda x: x%2==0, f_li))} \n",
        f"Количество нечетных элементов второго файла: {list(filter(lambda x: x % 2, s_li))} \n"
    ])
