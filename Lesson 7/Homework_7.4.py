import random


def common_elements():
	list_1 = []
	list_2 = []
	start_number = 1
	for _ in range(random.randrange(1, 100)):
		while True:
			if start_number % 3 != 0:
				start_number += 1
			else:
				list_1.append(start_number)
				start_number += 1
				break

	start_number = 1
	for _ in range(random.randrange(1, 100)):
		while True:
			if start_number % 5 != 0:
				start_number += 1
			else:
				list_2.append(start_number)
				start_number += 1
				break
	set1 = set(list_1)
	set2 = set(list_2)
	return set1.intersection(set2)


print(common_elements())
