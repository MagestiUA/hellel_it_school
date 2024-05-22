from inspect import isgenerator
from typing import Generator


def prime_generator(end: int) -> Generator[int, None, None]:
	"""Generator of prime numbers from 2 to 'end'
	end: end number, integer
	"""
	if not isinstance(end, int):
		raise TypeError('Argument "end" must be integer')
	if end < 2:
		raise ValueError('Argument "end" must be more than 1')
	for numbers in range(2, end + 1):
		# старий варіант коду, але теж працює
		# list_of_divisors = [True,]
		# for i in range(2, int(numbers ** 0.5) + 1):
		# 	if numbers % i != 0:
		# 		list_of_divisors.append(True)
		# 	else:
		# 		list_of_divisors.append(False)
		# if all(list_of_divisors):
		# 	yield numbers
		# далі новий варіант коду, зменшив на скільки зміг
		if all(numbers % i != 0 for i in range(2, int(numbers ** 0.5) + 1)):
			yield numbers


if __name__ == '__main__':
	gen = prime_generator(1)
	assert isgenerator(gen) is True
	assert list(prime_generator(10)) == [2, 3, 5, 7]
	assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
	assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	print('Ok')
