while True:
	x = int(input('Input first number and press Enter: \n'))
	operation = input('Input operation (+, -, *, /) and press Enter\n')
	y = int(input('Input second number and press Enter: \n'))
	if operation == '+':
		print(x + y)
	elif operation == '-':
		print(x - y)
	elif operation == '*':
		print(x * y)
	elif operation == '/':
		if y != 0:
			print(x / y)
		else:
			print('''Error, you can't divide by zero''')
	else:
		print('unknown operation')
	approval = input('Do you want to continue? (Yes or y)\n')
	approval = approval.lower()
	if approval == 'yes' or approval == 'y':
		continue
	break
	