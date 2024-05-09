import string


def say_hi(name: str, age: int) -> str:
	if not isinstance(name, str) or not isinstance(age, int):
		raise TypeError('Argument "name" must be string and argument "age" must be integer.')

	if len(name) == 0:
		raise ValueError('Name must not be empty')
	
	for char in name:
		if char not in string.ascii_letters:
			raise ValueError('Do not use special characters and numbers in the name')
	
	if not 0 < age < 120:
		raise ValueError('Age must be more than 0 and less than 120')
	
	name = name.title()
	return f"Hi. My name is {name} and I'm {age} years old"


if __name__ == '__main__':
	assert say_hi("Alex", 25) == "Hi. My name is Alex and I'm 25 years old"
	assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
	print('ОК')
