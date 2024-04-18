# я б робив так
try:
	numb = input('Type a four-digit number and press Enter\n')
	numb = int(numb)
	if len(str(numb)) != 4:
		print(f'You type {len(str(numb))} symbols, not 4')
	else:
		for char in str(numb):
			print(char)
except ValueError:
	print('You type not a number')


# якщо слідувати всім іструкціям з ДЗ, то має бути якось так
numb = int(input('Type a four-digit number\n'))
print(numb // 1000)
print((numb // 100) % 10)
print((numb // 10) % 10)
print((numb // 1) % 10)