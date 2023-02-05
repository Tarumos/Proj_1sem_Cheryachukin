from random import randint

length = randint(2, 4)
matrix = [[randint(-10, 10) for _ in range(length)] for _ in range(length)]

for row in matrix:
    print(*row, sep="\t")

print()
for row_index in range(len(matrix)):
    matrix[row_index] = matrix[row_index][:-1] + [-1]

for row in matrix:
    print(*row, sep="\t")
# Вариант 29