from typing import Tuple


class Rectangle:
	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height

	def get_square(self) -> int:
		return self.width * self.height

	def __eq__(self, other: object) -> bool:
		if isinstance(other, Rectangle):
			return self.get_square() == other.get_square()
		return False

	def __add__(self, other: 'Rectangle') -> 'Rectangle':
		if isinstance(other, Rectangle):
			new_area = self.get_square() + other.get_square()
			side_1, side_2 = self.find_sides(new_area)
			return Rectangle(side_1, side_2)
		raise TypeError('Actions can be performed only on objects of the Rectangle class')

	def __mul__(self, n: int) -> 'Rectangle':
		if isinstance(n, int):
			new_area = self.get_square() * n
			side_1, side_2 = self.find_sides(new_area)
			return Rectangle(side_1, side_2)
		raise TypeError('Argument must be an integer')

	def __str__(self):
		return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"
	
	@staticmethod
	def find_sides(new_area: int) -> Tuple[int, int]:
		factor_pairs = []
		for i in range(1, int(new_area ** 0.5) + 1):
			if new_area % i == 0:
				factor_pairs.append((i, new_area // i))
		factor_pairs.sort()
		return factor_pairs[-1]


if __name__ == '__main__':
	r1 = Rectangle(2, 4)
	r2 = Rectangle(3, 6)
	r3 = Rectangle(4, 2)
	assert r1.get_square() == 8
	assert r2.get_square() == 18
	assert r1 == r3
	
	r3 = r1 + r2
	assert r3.get_square() == 26
	
	r4 = r1 * 4
	assert r4.get_square() == 32
	
	assert Rectangle(3, 6) == Rectangle(2, 9)
	print('OK')
