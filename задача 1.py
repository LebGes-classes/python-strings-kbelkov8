input_string = input("Введите строку: ") + " "

list_words = []
word = ""
new_str = ""

for simbol in input_string:

    if simbol == " ":
        list_words.append(word + " ")
        word = ""
    elif simbol != " ":
        word += simbol

for slovo in list_words[::-1]:
    new_str += slovo

print(new_str)