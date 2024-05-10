import string


def is_palindrome(text: str) -> bool:
	"""
	Checks if text is palindrome
	:param text: string value, which you want to check
	:return: True if text is palindrome, else False
	"""
	
	if not isinstance(text, str):
		raise TypeError('Argument "text" must be string')
	if not text:
		raise TypeError('Argument "text" must not be empty')
	only_letters = ''.join(symbol for symbol in text if symbol in string.ascii_letters+string.digits).lower()
	if only_letters == only_letters[::-1]:
		return True
	return False


if __name__ == '__main__':
	assert is_palindrome('A man, a plan, a canal: Panama') is True
	assert is_palindrome('0P') is False
	assert is_palindrome(',_!/.%a.') is True
	assert is_palindrome(',_!/.%aurora') is False
	print("ОК")
