def find_unique_value(some_list: list) -> int:
	"""
	Find unique value in list, whose contains only digits
	:param some_list: list, elements which contains only digits
	:return: unique value
	"""
	
	if not isinstance(some_list, list):
		raise TypeError('Argument "some_list" must be integer or float')
	for el in some_list:
		if not isinstance(el, int | float):
			raise TypeError('Elements of argument "some_list" must be integer or float')
	for el in some_list:
		if some_list.count(el) == 1:
			return el


if __name__ == '__main__':
	assert find_unique_value([1, 2, 1, 1]) == 2
	assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
	assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5
	assert find_unique_value([5, 5, 5, 2, 2, 2]) is None
	print("ОК")
	