import string


ambit = input('Введіть потрібний діапазон в форматі "a-z"/"A-Z"/"a-Z" та натисніть Enter: \n')
first_letter = string.ascii_letters.index(ambit[0])
last_letter = string.ascii_letters.index(ambit[2])
print(string.ascii_letters[first_letter:last_letter + 1])
