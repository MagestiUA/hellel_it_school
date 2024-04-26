list_1 = [0, 1, 7, 2, 4, 8]
list_2 = [1, 3, 5]
list_3 = [6]
list_4 = []


#  якщо використовувати тільки пройдений матеріал, то код такий:
tmp_list = list_1[:]
if len(tmp_list) > 0:
	sum_el = 0
	for el in tmp_list[::2]:
		sum_el += el
	sum_el = sum_el * tmp_list[-1]
	print(sum_el)
else:
	print(0)


#  можна використовувати в вигляді функції, та передавати потрібний список
def work_wit_lists(some_list):
	tmp2_list = some_list[:]
	if len(tmp2_list) > 0:
		sum_elem = sum(elem for elem in tmp2_list[::2])
		return sum_elem * tmp2_list[-1]
	else:
		return 0


print(work_wit_lists(list_1))
