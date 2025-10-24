import re

text = input("Введите текст: ")

list_word = re.findall(r'[A-Za-zА-Яа-я]+', text)
set_word = set(list_word)
dict_word = dict()
return_words = list()
sort_list = []

for word in set_word:
    dict_word[word] = 0

for count_word in list_word:
    dict_word[count_word] += 1

for element in dict_word:
    sort_list.append([dict_word[element], element])

schet = 1

while schet < len(sort_list):
    for slovo in range(len(sort_list) - schet):
        if sort_list[slovo][0] < sort_list[slovo + 1][0]:
            sort_list[slovo], sort_list[slovo + 1] = sort_list[slovo + 1], sort_list[slovo]

    schet += 1

for itog_word in sort_list:
    return_words.append(itog_word[1])

print(return_words[:5])