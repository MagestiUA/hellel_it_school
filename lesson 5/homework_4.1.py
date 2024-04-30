import string


some_text = input('Enter some text: \n')
some_text = some_text.title()
some_text = ''.join(symbol for symbol in some_text if symbol not in string.punctuation + ' ')
hashtag = '#' + some_text
if len(hashtag) > 140:
	hashtag = hashtag[:140]

print(hashtag)
