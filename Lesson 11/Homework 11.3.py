def is_even(number: int) -> bool:
	""" Перевірка чи є парним число, повертає True або False
	number: ціле число
	"""
	even_number = [2, 4, 6, 8, 0]
	if not isinstance(number, int):
		raise TypeError('Argument "number" must be integer')
	if int(str(number)[-1]) in even_number:
		return True
	return False


if __name__ == '__main__':
	assert is_even(2) is True
	assert is_even(3) is False
	assert is_even(2494563894038**2) is True
	assert is_even(1056897**2) is False
	assert is_even(24945638940387**3) is False
	print('Ok')
