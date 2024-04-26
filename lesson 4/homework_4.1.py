list_1 = [0, 1, 0, 12, 3]
list_2 = [0]
list_3 = [1, 0, 13, 0, 0, 5]
list_4 = [9, 0, 7, 31, 0,45, 0, 45, 0, 45, 0, 0, 96, 0]


#  якщо використовувати тільки пройдений матеріал, то код такий:
#  замінюємо 1 цифру в рядку 8, та перевіряємо на інших списках.
list_tmp = list_4.copy()
for el in list_tmp:
	if el == 0:
		list_tmp.append(list_tmp.pop(list_tmp.index(el)))
print(list_tmp)


#  можна використовувати в вигляді функції, та передавати потрібний список
def work_wit_lists(some_list):
	list_tmp2 = some_list.copy()
	for elem in list_tmp2:
		if elem == 0:
			list_tmp2.append(list_tmp2.pop(list_tmp2.index(elem)))
	print(list_tmp2)


work_wit_lists(list_4)
