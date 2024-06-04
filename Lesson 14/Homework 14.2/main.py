from Class_Student import Student
from Class_Group import Group
from Class_Exception import GroupIsFullException


if __name__ == '__main__':
	st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
	st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
	gr = Group('PD1')
	gr.add_student(st1)
	gr.add_student(st2)
	print(gr)
	assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
	assert gr.find_student('Jobs2') is None
	gr.delete_student('Taylor')
	print(gr)  # Only one student
	st3 = Student('Male', 31, 'Noah', 'Smith', 'AN141')
	st4 = Student('Female', 26, 'Emma', 'Blacksmith', 'AN143')
	st5 = Student('Male', 33, 'Liam', 'Jonson', 'AN144')
	st6 = Student('Female', 24, 'Olivia', 'Jones', 'AN146')
	st7 = Student('Male', 25, 'William', 'Brown', 'AN147')
	st8 = Student('Female', 28, 'Ava', 'Wilson', 'AN148')
	st9 = Student('Male', 23, 'Mason', 'Davis', 'AN149')
	st10 = Student('Female', 29, 'Isabella', 'Miller', 'AN150')
	st11 = Student('Male', 31, 'Benjamin', 'Williams', 'AN151')
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