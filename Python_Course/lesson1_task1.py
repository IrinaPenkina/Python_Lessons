# import math

# m = int(input('Введите длину маршрута: '))
# n = 700
# print(math.ceil(m/n))


# m = int(input('Введите длину маршрута: '))
# n = 700
# if m > n:
#     print(m//n + 1)
# elif m == 0:
#     print(0)
# else:
#     print(1)


m = int(input('Введите длину маршрута: '))
n = 700
a1 = m//n
a2= bool(m%n)
a2 = int(a2)
rez = a1 + a2
print(rez)

