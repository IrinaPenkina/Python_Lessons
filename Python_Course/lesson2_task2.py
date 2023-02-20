# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input('Введите натуральное число: '))
# fib_1 = 0
# fib_2 = 1
# fibonacci = 1
# n = 1

# while fibonacci <= a:
#     fibonacci = fib_1 + fib_2
#     fib_1 = fib_2
#     fib_2 = fibonacci
#     n += 1

# if a == fib_1:
#     print(n)
# else:
#     print(-1)

my_num = int(input('Введите натуральное число больше 1: '))

my_list = []
a, b = 0, 1
while a < my_num + 1:
    my_list.append(a)
    a, b = b, a + b
print(my_list)

if my_num in my_list:
    print(len(my_list))
else:
    print(-1)

