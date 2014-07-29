'''
	Another interesting problem I came across was the literal representation of numbers.
	Given a number, we must return its literal/oral representation

	For example:
	"1" => "11" one one
	"11" => "21" two one
	"21" => "1211" one two one one

	INPUT:
		A number in string representation

	OUTPUT:
		The literal representation
'''

def get_literal_rep(num):
	if len(set(num)) == 1:
		return str(len(num)) + num[0]

	res = ""

	for idx, c in enumerate(num):
		sub, count = num[idx+1:], 1
		if len(sub) > 0:
			for sub_c in sub:
				if sub_c != c:
					break
				count += 1
			res += str(count) + c
		else:
			if num[idx-1] != c:
				res += str(count) + c

	return res


if __name__ == '__main__':
	print get_literal_rep("1")
	print get_literal_rep("11")
	print get_literal_rep("21")
	print get_literal_rep("1211")