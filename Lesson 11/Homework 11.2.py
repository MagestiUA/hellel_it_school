from inspect import isgenerator
from typing import Generator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
	"""Generator of cube numbers until result <= 'end'
	end: end number, integer
	"""
	if not isinstance(end, int):
		raise TypeError('Argument "end" must be integer')
	if end <= 0:
		raise ValueError('Argument "end" must be more than 0')
	i = 2
	while end >= i**3:
		yield i**3
		i += 1


if __name__ == '__main__':
	gen = generate_cube_numbers(1)
	assert isgenerator(gen) is True
	assert list(generate_cube_numbers(1)) == []
	assert list(generate_cube_numbers(7)) == []
	assert list(generate_cube_numbers(10)) == [8]
	assert list(generate_cube_numbers(100)) == [8, 27, 64]
	assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
	print('Ok')
