import string
import keyword


def check_variable_name():
	variable_name = input('Input name of variable: \n')
	disable_symbols = string.punctuation.replace('_', '') + ' '
	if variable_name[0].isdigit():
		return False
	if not variable_name.islower() and variable_name != '_':
		return False
	if any(symbols in disable_symbols for symbols in variable_name):
		return False
	if variable_name != '_' and '_' in variable_name and len(set(variable_name)) == 1:
		return False
	if variable_name in keyword.kwlist:
		return False
	return True


if __name__ == '__main__':
	while True:
		print(check_variable_name())
