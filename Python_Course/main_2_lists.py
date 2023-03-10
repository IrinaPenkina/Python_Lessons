# Способы задания списка
# list_1 = []
# list_1 = list()
# list_1 = [1, 4, 8, 3]
# print(list_1) # распечатка со скобками
# print(*list_1) #распечатка без скобок и запятых

# for i in list_1:
#     print(i)  # i принимает значения, как элементы list_1

# print(len(list_1))  # вывод длины списка

# print(list_1[0])  # 1 // вывод первого элемента списка с начала (слева)

# print(list_1[-1])   #  3 // вывод первого с конца элемента списка


# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавили элемент 8
# print(list_1)
# list_1.append(85)  # добавии элемент 85
# print(list_1)


# Добавление в список
# list_1 = []
# print(list_1)
# for i in range (5):
#     list_1.append(i)
#     print(list_1)

# Удаление из списка - по умолчанию с конца
# list_1 = [3, 7, 5, 8, 0]
# # print(list_1.pop)  # возвращает и удаляет из списка последний элемент
# a = list_1.pop()
# print(a)

# Вывод и удаление конкретного элемента из списка
# list_1 = [4, 7, 1, 9]
# print(list_1)
# print(list_1.pop(0))  # распечатает нулевой элемент
# print(list_1)  # [7, 1, 9]

# Добавление элемента на нужное место
# list_1 = [4, 7, 1, 9]
# print(list_1)
# list_1.insert(2, 12)  # вставит на второе место элемент 12
# print(list_1)  # [4, 7, 12, 1, 9]

# Срезы списка
# list_1 = [4, 7, 1, 9, 2, 13]
# print(list_1[:])  # весь
# print(list_1[:2])  # два первых элемента
# print(list_1[len(list_1)-2:]) # два последних элемента
# print(list_1[::2]) # с нулевого через один до конца


# Быстрое задание списка: list comprehension
list_2 = [3 for i in range(5)]
print(list_2)

# Задать список из последовательности чисел от 1 до 10
list_3 = [i for i in range (1, 11)]
print(list_3)

# Задать список из последовательности четных чисел от 1 до 10
list_4 = [i for i in range (1, 11) if i % 2 == 0]
print(list_4)

# Задать пары четных чисел от 1 до 20 через кортеж
list_5 = [(i, i) for i in range (1, 21) if i % 2 == 0]
print(list_5)
list_6 = [(i, i*i) for i in range (1, 21) if i % 2 == 0]
print(list_6)




