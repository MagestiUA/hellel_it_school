def popular_words(text: str, words: list[str]) -> dict:
	"""
	Function returns dict with words popularity in text.
	:param text: string
	:param words: list of strings
	:return: dict: {word: count of word in text}
	"""
	if not isinstance(words, list):
		raise TypeError('Argument "words" must be list')
	for word in words:
		if not isinstance(word, str):
			raise TypeError('Elements of argument "words" must be str')
	if not isinstance(text, str):
		raise TypeError('Argument "text" must be str')
	
	word_popularity = {}
	for word in words:
		word_popularity[word.lower()] = text.lower().split().count(word.lower())
	return word_popularity


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
assert popular_words('''When I was One I had just beguN When I Was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
print('OK')
