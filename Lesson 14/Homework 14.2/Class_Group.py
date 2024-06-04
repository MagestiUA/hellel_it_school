from Class_Student import Student
from Class_Exception import GroupIsFullException


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