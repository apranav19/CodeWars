'''
	A popular programming challenge.
	Let's say we have a function that produces patterns as follows:
	f(0) = 1
	f(1) = 11
	f(2) = 21
	f(3) = 1211
	f(4) = 111221
	f(5) = 312211
	@author - Pranav Angara
'''

def find_pattern(num):
	res = str(1)

	while num>0:
		prev_c, text, ct = res[0], [], 1
		for i in xrange(1,len(res)):
			if res[i] != prev_c:
				text.append(str(ct)+prev_c)
				prev_c = res[i]
				ct = 1
			else:
				ct += 1
		text.append(str(ct)+prev_c)
		res = ('').join(text)
		num -= 1

	return int(res)


if __name__ == '__main__':

	for i in xrange(10):
		pattern = find_pattern(i)
		print 'Pattern # ' + str(i) + ' ' + str(pattern)