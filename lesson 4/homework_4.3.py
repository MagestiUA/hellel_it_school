import random

first_list = [random.randint(1, 1000) for _ in range(random.randint(3, 10))]
print(first_list)
second_list = first_list[0:4:2]
second_list.append(first_list[-2])
print(second_list)
