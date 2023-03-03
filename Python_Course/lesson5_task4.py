# Задача №37. 
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


# def reverse (n):
#     if n == 0:
#         return ' '
#     val = input()
#     return reverse(n-1) + f' {val}'    

# print(reverse(n))



text = str(input('Введите символы: '))

# 1 способ

# def reversed3(variable): 
#     if len(variable) == 1:
#         return variable
#     return variable[-1] + reversed3(variable[:-1])

# n = reversed3(text)
# print(n)


# 2 способ

# def reversed4(variable):
#     res=''.join(reversed(variable))
#     return res

# n = reversed4(text)
# print(n)


# 3 способ

n = text[::-1]
print(n)