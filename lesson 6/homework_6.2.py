input_seconds = input('Введіть кількість секунд для переводу інший формат часу. \nВедене число має бути цілим, складись тільки з цифр та більшим або дорівнювати 0, і бути меншим за 8640000.: \n')
if not input_seconds.isdigit():
	print('Введено не вірне значення. Вводити потрібно лише цифри!!')
elif int(input_seconds) >= 8640000:
	print('Ви ввели число більше або рівне 8640000!')
elif 0 <= int(input_seconds) < 8640000:
	days = int(input_seconds) // 86400
	hours = int(input_seconds) // 3600 % 24
	minutes = int(input_seconds) % 3600 // 60
	seconds = int(input_seconds) % 3600 % 60
	days_text = ''
	if days in range(11, 15):
		days_text = 'днів'
	elif days % 10 == 1:
		days_text = 'день'
	elif 1 < days % 10 < 5:
		days_text = 'дні'
	else:
		days_text = 'днів'
	print(f'{input_seconds} секунд = {days} {days_text}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
