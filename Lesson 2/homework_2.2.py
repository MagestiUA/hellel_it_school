numb = int(input('Type a five-digit number and press Enter\n'))
sumb_1 = (numb // 1) % 10
sumb_2 = (numb // 10) % 10
sumb_3 = (numb // 100) % 10
sumb_4 = (numb // 1000) % 10
sumb_5 = numb // 10000
reversed_numb = sumb_1 * 10000 + sumb_2 * 1000 + sumb_3 * 100 + sumb_4 * 10 + sumb_5
print(reversed_numb)
print(type(reversed_numb))
# строки не використав