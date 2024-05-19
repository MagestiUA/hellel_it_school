from inspect import isgenerator


def some_function(x: int) -> int:
	return x ** 2


def some_gen(begin: int, end: int, func: callable):
	"""
	Генераторна функція, яка формує послідовність чисел від begin до end за допомогою функції func
	'begin': перший елемент послідовності
	'end': кількість елементів у послідовності
	'func': функція, яка формує значення для послідовності
	"""
	if not isinstance(begin, int):
		raise TypeError('Argument "begin" and "end" must be integer')
	if not isinstance(end, int):
		raise TypeError('Argument "end" must be integer')
	if not callable(func):
		raise TypeError('Argument "func" must be function')
	for _ in range(end):
		yield begin
		begin = func(begin)


if __name__ == '__main__':
	gen = some_gen(2, 4, some_function)
	assert isgenerator(gen) is True
	assert list(gen) == [2, 4, 16, 256]
	print('OK')
