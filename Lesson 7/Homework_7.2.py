import string


def correct_sentence(text: str) -> str:
	if not isinstance(text, str):
		raise TypeError('Input must be a string.')
	if len(text) == 0:
		raise TypeError('Input text must not be empty.')
	while text[0] not in string.ascii_letters:
		text = text[1:]
	strings_list = text.split('.')
	text = '. '.join(el.strip().capitalize() for el in strings_list).strip()
	while text[-1] not in string.ascii_letters:
		text = text[:-1]
	if not text.endswith('.'):
		text += '.'
	return text


if __name__ == '__main__':
	assert correct_sentence("__!!__..11greetings, friends!!_.1") == "Greetings, friends."
	assert correct_sentence("hello") == "Hello."
	assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
	assert correct_sentence("Greetings, friends.") == "Greetings, friends."
	assert correct_sentence("greetings, friends.") == "Greetings, friends."
	print('ОК')
