# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

s = ('a a a b c a a d c d d')
lst_1 = s.split(' ')
lst_2 = []

for item in lst_1:
    if lst_2.count(item) >= 1:
        print(f'{item}_{lst_2.count(item)}', end=' ')
    else:
        print(item, end=' ')
    lst_2.append(item)

# Другие решения
