#Кортеж - неизменяемый список

t = ()
print(type(t))

t = (1, 3,)
print(type(t))

v = [5, 3, 7]
print(v)
print(type(v))
v = tuple(v)
print(v)
print(type(v))

# Распаковка кортежа
a, b, c = v
print(a, b, c)

# В отличие от списка кортеж не может быть изменен.
# Все другие операции можно проводить так же, как и со списокм.