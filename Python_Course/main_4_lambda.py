# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 7)


# Переход к лямбда:

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a,b: a + b

# math(calk1, 5, 45)


# Еще короче:

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)


# Задача.
# В списке хранятся числа. 
# Нужно выбрать только четные числа и составить список пар: (число; квадрат числа).

# Простой метод

# data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)


# Метод с функциями

def select(f, col):
    return [f(x) for x in col]
# Возвращает функцию, примененную ко всем элементам списка 

def where(f, col):
    return [x for x in col if f(x)]
# Возвращает элемент из списка при соблюдении условия 

data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
res = select(int, data)  # преобразует все элементы в целые числа
print(res)
res = where(lambda x: x % 2 == 0, res)  # выводит только четные элементы из списка
print(res)
res = list(select(lambda x: (x, x**2), res)) # создает кортеж, а потом преобразует в список
print(res)

