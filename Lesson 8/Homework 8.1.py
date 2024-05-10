def add_one(some_list: list) -> list:
	"""
	Adding 1 to list
	:param some_list: list
	:return: list
	"""
	
	if not isinstance(some_list, list):
		raise TypeError('Argument "some_list" must be list')
	for el in some_list:
		if not isinstance(el, int):
			raise TypeError('Elements of argument "some_list" must be int')
	str_list = ''.join(str(el) for el in some_list)
	int_numb = int(str_list) + 1
	new_list = list(int(el) for el in str(int_numb))
	return new_list


if __name__ == '__main__':
	assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
	assert add_one([9, 9, 9]) == [1, 0, 0, 0]
	assert add_one([0]) == [1]
	assert add_one([9]) == [1, 0]
	print("ОК")
	