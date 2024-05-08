def second_index(text: str, some_str: str) -> int | None:
	if not isinstance(text, str) or not isinstance(some_str, str):
		raise TypeError("Both arguments must be strings.")
	
	if not some_str:
		#  some_str не повинна бути пустою інакше поверне індекс 1
		return None
	
	second_char_index = text.find(some_str, text.find(some_str) + 1)
	return second_char_index if second_char_index != -1 else None


assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo") == 10
assert second_index("Hello, he11o", "") is None
print('ОК')
