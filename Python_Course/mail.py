
"""
n = 'str\'ing'

print(n)
print(type(n))
"""
"""
a = 5
b = 4.76
c = 'hello'

print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a,b,c))
"""

# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

"""
g = 5.395766
f = 6.383948573
print(round(g*f, 3))
"""

"""
n = int(input('Введите целое число: '))
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print (i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1
"""

"""
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "+"
    print(line)
"""

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # количество символов
print('ещё' in text) # true или false, ещё в тексте 
print(text.lower()) # перевод всех букв в нижний регистр
print(text.upper()) # перевод всех букв в верхний регистр
print(text.replace('ещё', 'ЕЩЁ')) # замена
