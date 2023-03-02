#  Задача 31.
# Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13


# def fib(N):
#     if N in(0,1):
#         return N
    
#     return fib(N-1) + fib(N-2)


fib = lambda N: N if N in (0, 1) else fib(N-1) + fib(N-2)

print(fib(7))