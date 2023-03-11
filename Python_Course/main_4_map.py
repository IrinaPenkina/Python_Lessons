# Задача. 
# С клавиатуры вводится набор чисел, в качестве разделителя - пробел.
# Этот набор будет считан в качестве строки.
# Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'
print(data)

data = list(map(int, data.split()))
print(data)


# Задача.
# В списке хранятся числа. 
# Нужно выбрать только четные числа и составить список пар: (число; квадрат числа).

def where(f, col):
    return [x for x in col if f(x)]
# Возвращает элемент из списка при соблюдении условия 

data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
res = map(int, data)  # преобразует все элементы в целые числа
print(res)
res = where(lambda x: x % 2 == 0, res)  # выводит только четные элементы из списка
print(res)
res = list(map(lambda x: (x, x**2), res)) # создает кортеж, а потом преобразует в список
print(res)

# map = select из предыдущей задачи
# def select(f, col):
#     return [f(x) for x in col]

