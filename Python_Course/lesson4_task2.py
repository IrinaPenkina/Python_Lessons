# Задача №27. 
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 19

# #1 решение
# text = "She sells.  sea shells   on the sea shore; "
# text1 = text.split()
# text2 = []
# for item in text1:
#     if item not in text2:
#         text2.append(item)

# print(text1)
# print(f'Всего слов: {len(text1)}')        
# print(text2)
# print(f'Уникальных слов: {len(text2)}')


#2 Решение

import re

string = "She sells.  sea shells   on the sea shore; "
word_list = re.findall(r'\b\w+\b', string)

print("Количество слов в строке:", len(word_list))