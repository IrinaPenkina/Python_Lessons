# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import *
# n = int(input('Задайте количество оценок: '))
# grades = [randint(1, 5) for _ in range(n)]
# print(grades)

# min_grades = min(grades)
# max_grades = max(grades)

# for i, val in enumerate(grades):
#     if val == max_grades:
#         grades[i] = min_grades

# print(grades)


# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Меняет только один мин с одним макс!
# minIndex = grades.index(min(grades))
# maxIndex = grades.index(max(grades))
# grades[minIndex], grades[maxIndex] = grades[maxIndex], grades[minIndex]

# print(*grades, sep=' ')


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# list(enumerate(seasons))
#  [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

m = int(input('Задайте количество оценок: '))
a = [randint(1, 5) for _ in range(m)]
print(a)

a[:] = map(lambda x: min(a) if x == max(a) else max(a) if x == min(a) else x, a)
print(a)