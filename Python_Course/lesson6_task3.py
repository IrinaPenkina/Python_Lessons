# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:          Вывод:
# 1 2 3 2 3      2


# n = int(input('Задайте количество элементов первой строки: '))
# lst = [int(input('Введите число массива: ')) for i in range(n)]
# print(*lst)


# Решение через цикл:
# count = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)

# Решение через метод count:
# count = 0
# for i in range(n-1):
#     count += lst[i+1:].count(lst[i])
# print(count)

# Решение через рекурсию:

from random import randrange

def func(lst: list) -> int:
    el, *lst = lst  # берем элемент и срез остального списка
    if lst:  # если не пустой список
        return func(lst) + lst.count(el)
    return 0   # если пустой, возвращаем ноль

if __name__ == '__main__':  # паттерн изолирования, не дает импортировать то, что в нем. можно импортировать только до него
    n = int(input('n =  '))
    lst = [randrange(n) for _ in range(n)]
    print(lst)
    print(func(lst))


