def difference(*args: int | float) -> int | float:
	"""
	Find difference between max and min elements
	:param args: numerical values are written in numbers
	:return: difference between max and min elements in int or float
	"""
	for el in args:
		if not isinstance(el, int | float):
			raise TypeError('Arguments must be int or float')
	if len(args) == 0:
		return 0
	return round((max(args) - min(args)), 2)


assert difference(1, 2, 3) == 2
assert difference(5, -5) == 10
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
assert difference(1) == 0
assert difference() == 0

print('OK')
