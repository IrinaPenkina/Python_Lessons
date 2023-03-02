# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import *
n = int(input('Задайте количество оценок: '))
grades = [randint(1, 5) for _ in range(n)]

min_grades = min(grades)
max_grades = max(grades)

# for i in range(len(grades)):
#     if grades[i] == max:
#         grades[i] = min

for i, val in enumerate(grades):
    if val == max_grades:
        grades[i] = min_grades

print(grades)