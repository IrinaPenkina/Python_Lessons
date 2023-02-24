# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4, 4, 4]
# list_new = sorted(list)
# print(list_new)
# count = 1

# for i in range(len(list_new) - 1):
#     if list_new[i] != list_new[i + 1]:
#         count += 1
# print(count)


lst = [1, 1, 2, 0, -1, 3, 4, 4, 4, 4]
lst_2 = []

for item in lst:
    if item not in lst_2:
        lst_2.append(item)
print(lst_2)
print(len(lst_2))
