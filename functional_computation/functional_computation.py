'''
	This problem is adapted from codewars.com.
	Using functional programming, the idea is to 'functionalize' mathematical operations such as +,-,*,/
	For numbers 0 - 9, we need to represent them as functions.

	For example:
	To compute 7 + 3 = 10, 
	we can represent the equation above as:
	seven(add(three())) = 10

	The problem simply requires 2 operands and an operator
'''

# Util functions
def get_val(operator, operand):
	if operator:
		return operator(operand)
	return operand

# Begin functions for operators

def add(n):
	return lambda x: x + n

def subtract(n):
	return lambda x: x - n

def multiply(n):
	return lambda x: x * n

def divide(n):
	return lambda x: x/n

# Begin functions for numbers 0-9
def zero(n=None):
	return get_val(n, 0)

def one(n=None):
	return get_val(n, 1)

def two(n=None):
	return get_val(n, 2)

def three(n=None):
	return get_val(n, 3)

def four(n=None):
	return get_val(n, 4)

def five(n=None):
	return get_val(n, 5)

def six(n=None):
	return get_val(n, 6)

def seven(n=None):
	return get_val(n, 7)

def eight(n=None):
	return get_val(n, 8)

def nine(n=None):
	return get_val(n, 9)

if __name__ == '__main__':
	
	# Add 1 + 1
	print one(add(one()))

	# Subtract 6 - 3
	print six(subtract(three()))

	# Multiply 9 x 5
	print nine(multiply(five()))

	# Divide 8 / 4
	print eight(divide(four()))

	# Some more complicated like 7 + (3 * (8 - (6 / 2)))
	print seven(add(three(multiply(eight(subtract(six(divide(two()))))))))

