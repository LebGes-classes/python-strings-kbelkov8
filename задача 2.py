word = ""
alphabet_stroch = "abcdefghijklmnopqrstuvwxyz"
alphabet_propis = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
K = 0
dot = -1
returntext = ""
text = " "

while dot == -1:
    text = input("Введите текст с точкой на конце!: ")

    dot = text.find(".")

for symbol1 in range(dot + 1):
    if text[symbol1] == "," or text[symbol1] == " " or text[symbol1] == ".":

        if (K < len(word)) and (len(word) <= 20):
            K = len(word)
        elif len(word) > 20:
            K = 20
            word = ""

        word = ""
    else:
        word += text[symbol1]

for symbol2 in range(dot):

    if text[symbol2] in alphabet_stroch:
        index_letter = alphabet_stroch.index(text[symbol2]) + K

        if index_letter > 25:
            letter1 = alphabet_stroch[index_letter - 26]
        else:
            letter1 = alphabet_stroch[index_letter]

        returntext += letter1
    elif text[symbol2] in alphabet_propis:
        index_letter = alphabet_propis.index(text[symbol2]) + K

        if index_letter > 25:
            letter2 = alphabet_propis[index_letter - 26]
        else:
            letter2 = alphabet_propis[index_letter]

        returntext += letter2
    else:
        returntext += text[symbol2]

print(returntext + text[dot:])