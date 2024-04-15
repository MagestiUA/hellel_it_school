print('Hellow world')
print('Hellow world\n')
print('Hellow world ' * 50, '\n')
text = 'Hellow world'
int_1 = 25
int_2 = 5
int_3 = 0
print(text + ' ' + str(int_1 * int_2))
print(text + '\n ' + str(int_1 + int_2))
try:
	print(int_2 / int_3)
except Exception as err:
	print(err)