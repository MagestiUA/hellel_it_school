import codecs
import re


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
	"""
	Deletes html tags from html file
	:param html_file: name of html file which you want to clean
	:param result_file: name of file where cleaned text will be saved
	:return:
	"""
	with codecs.open(html_file, 'r', 'utf-8') as file:
		html = file.read()
	clean_text = re.sub(r'<.*?>', '', html, flags=re.DOTALL)
	with codecs.open(result_file, 'w', 'utf-8') as file:
		for line in clean_text.split('\n'):
			if line and not line.isspace():
				file.write(line + '\n')


if __name__ == '__main__':
	delete_html_tags(html_file='draft.html', result_file='cleaned.txt')
	