# Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!
# ДЗ необхідно здати наступним чином:
# Посилання на файл ДЗ на GitHub:
# Або
# Додайте файл до відповіді на домашнє завдання в систему управління навчанням (ЛМС).
x = int(input('Input first number and press Enter: \n'))
y = int(input('Input second number and press Enter: \n'))
operation = input('Input operation (+, -, *, /) and press Enter: \n')
if operation == '+':
	print(x + y)
elif operation == '-':
	print(x - y)
elif operation == '*':
	print(x * y)
elif operation == '/':
	if y == 0:
		print("Error, you can't divide by zero")
	else:
		print(x / y)
else:
	print('Error')

#як би я робив без опирання на пройдений матеріал:
def calc(x, y, operation):
	if operation == '+':
		return x + y
	elif operation == '-':
		return x - y
	elif operation == '*':
		return x * y
	elif operation == '/':
		if y != 0:
			return x / y
		else:
			return "Error, you can't divide by zero"
	else:
		return 'unknown operation'


def main():
	while True:
		try:
			x2 = int(input('Input first number and press Enter: \n'))
			y2 = int(input('Input second number and press Enter: \n'))
			operation2 = input('Input operation (+, -, *, /) and press Enter (or "q" to quit): \n')
			if operation2 == 'q':
				break
			print(calc(x2, y2, operation2))
		except Exception as err:
			print(err)
			break
if __name__ == "__main__":
	main()
