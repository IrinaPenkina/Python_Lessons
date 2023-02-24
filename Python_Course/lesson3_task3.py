# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# lst = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
# lst_new = []

# for item in lst:
#     for key in item:
#         val = item[key]
#         if val not in lst_new:
#             lst_new.append(val)
# print(lst_new)


lst = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

result = set()

for dct in lst:
    # print(dct.values())
    # print(type(dct.values()))
    # print(*dct.values())  # не индексируемый объект, но м.б. преобразован 
    result.add(*dct.values())
print(result)

