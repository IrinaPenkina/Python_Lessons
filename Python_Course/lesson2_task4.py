# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input('Задайте количество арбузов: '))
# mellons = []
# min_mellons = 15
# max_mellons = 1

# for i in range (n):
#     from random import randint
#     m = randint(1, 15)
#     if m > max_mellons:
#         max_mellons = m
#     if m < min_mellons:
#         min_mellons = m
#     mellons.append(m)

# print(mellons)
# print(f"{min_mellons}, {max_mellons}")

# import random
# n = int(input('Задайте количество арбузов: '))
# a = [random.randint (1, 15) for _ in range (n)]
# print(a)
# print(min(a), max(a))

from random import *
l1st = []
rang = int(input("Разброс веса от 1 до n"))
num = int(input("Количество арбузов: "))
for i in range(0, num):
    l1st.append(randint(1, rang))
print(l1st)
print(min(l1st), max(l1st))