from random import randint

matrix = [[randint(-10, 10) for _ in range(randint(3, 5))] for _ in range(5)]
for row in matrix:
    print(*row, sep="\t")

print()
matrix[2] = [randint(-10, 10) for _ in range(len(matrix[2]))]
for row in matrix:
    print(*row, sep="\t")
