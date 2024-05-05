some_number = input("Введіть будь яке ЦІЛЕ число (ЦИФРАМИ) та натисніть Enter: \n")
if some_number.isdigit():
	if int(some_number) <= 9:
		print(some_number)
	else:
		while int(some_number) > 9:
			product = 1
			for symbol in str(some_number):
				product *= int(symbol)
			some_number = str(product)
		print(some_number)

else:
	print("Ви ввели не число!")
