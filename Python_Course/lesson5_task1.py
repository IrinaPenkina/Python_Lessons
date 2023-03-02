# Задача 31.
# Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

n = int(input('Введите номер элемента: '))

def fib(a):
    if a == 0:
        return 0
    if a in [1,2]:
        return 1
    return fib(a-1) + fib(a-2)

fibonacci = []
for i in range (1, n):
    fibonacci.append(fib(i))

print (fib(n))
