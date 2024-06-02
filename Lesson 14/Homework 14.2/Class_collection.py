
class Human:
	def __init__(self, gender: str, age: int, first_name: str, last_name: str):
		self.gender = gender
		self.age = age
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self) -> str:
		return f'{self.first_name} {self.last_name}, {self.age} years old. {self.gender}'


class Student(Human):
	def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
		super().__init__(gender, age, first_name, last_name)
		self.record_book = record_book

	def __str__(self) -> str:
		return f'{self.first_name} {self.last_name}, {self.gender}. Record_book: {self.record_book}'
	
	def __eq__(self, other: object) -> bool:
		if isinstance(other, Student):
			return str(self) == str(other)
		return False
	
	def __hash__(self) -> int:
		return hash(str(self))


class GroupIsFullException(Exception):
	pass


class Group:
	def __init__(self, number: str):
		self.number = number
		self.group = set()

	def add_student(self, student: Student) -> None:
		if len(self.group) >= 10:
			raise GroupIsFullException('Group is full')
		self.group.add(student)

	def delete_student(self, last_name: str) -> None:
		student = self.find_student(last_name)
		if student:
			self.group.remove(student)

	def find_student(self, last_name: str) -> Student | None:
		return next((student for student in self.group if student.last_name == last_name), None)

	def __str__(self) -> str:
		all_students = '\n'.join(str(student) for student in self.group)
		return f'Number:{self.number}\n{all_students}'


if __name__ == '__main__':
	st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
	st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
	st3 = Student('Male', 31, 'Noah', 'Smith', 'AN141')
	st4 = Student('Female', 26, 'Emma', 'Blacksmith', 'AN143')
	st5 = Student('Male', 33, 'Liam', 'Jonson', 'AN144')
	st6 = Student('Female', 24, 'Olivia', 'Jones', 'AN146')
	st7 = Student('Male', 25, 'William', 'Brown', 'AN147')
	st8 = Student('Female', 28, 'Ava', 'Wilson', 'AN148')
	st9 = Student('Male', 23, 'Mason', 'Davis', 'AN149')
	st10 = Student('Female', 29, 'Isabella', 'Miller', 'AN150')
	st11 = Student('Male', 31, 'Benjamin', 'Williams', 'AN151')
	gr = Group('PD1')
	gr.add_student(st1)
	gr.add_student(st2)
	gr.add_student(st3)
	gr.add_student(st4)
	gr.add_student(st5)
	gr.add_student(st6)
	gr.add_student(st7)
	gr.add_student(st8)
	gr.add_student(st9)
	gr.add_student(st10)
	try:
		gr.add_student(st11)
	except GroupIsFullException as e:
		print(e)
	else:
		assert False, "Expected GroupFullException"
	print(gr)
	assert str(gr.find_student('Jobs')) == str(st1)
	assert gr.find_student('Jobs2') is None
	assert isinstance(gr.find_student('Jobs'), Student) is True
	gr.delete_student('Taylor')
	print(gr)
	gr.add_student(st11)
	print(gr)
	print('OK')
