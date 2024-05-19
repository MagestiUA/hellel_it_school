def is_even(digit: int) -> bool:
	""" Перевірка чи є парним число, повертає True або False
	digit: ціле число
	"""
	if not isinstance(digit, int):
		raise TypeError('Argument "digit" must be integer')
	return digit % 2 == 0


if __name__ == '__main__':
	assert is_even(2) is True
	assert is_even(5) is False
	assert is_even(0) is True
	assert is_even(10) is True
	assert is_even(20) is True
	assert is_even(13) is False
	print('OK')
