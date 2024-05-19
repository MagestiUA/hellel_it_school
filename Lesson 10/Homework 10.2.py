import string


def first_word(text: str) -> str:
	""" Пошук першого слова в тексті
	text: текст
	"""
	if not isinstance(text, str):
		raise TypeError('Argument must be string')
	if len(text) == 0:
		raise TypeError('Argument must not be empty')
	for char in string.punctuation.replace("'", ''):
		text = text.replace(char, ' ')
	return text.strip().split()[0]


if __name__ == '__main__':
	assert first_word("Hello world") == "Hello"
	assert first_word("greetings, friends") == "greetings"
	assert first_word("don't touch it") == "don't"
	assert first_word(".., and so on ...") == "and"
	assert first_word("hi") == "hi"
	assert first_word("Hello.World") == "Hello"
	print('OK')
