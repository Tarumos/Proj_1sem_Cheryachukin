# Вариант 29. Дан список A размера N и целое число K (1 < K < N). Преобразовать список, увеличив каждый его элемент
# на исходное значение элемента Ak.
a = []
n = int(input('Введите длину списка: '))
k = int(input('Введите число k: '))

for i in range(0, n):
    a.append(int(input('Введите числа, которые нужны в списке: ')))
print(a)
ak = a[k-1]

for i in range(0, n):
    a[i] += ak

print(a)