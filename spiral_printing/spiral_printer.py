'''
	The following function takes in a matrix (n x m)
	and prints the elements starting from the row, col point in a clock wise pattern
	Pre-condition: maze has at least 1 row and 1 col
'''
def print_clockwise(matrix):
	'''
		Let's assume we have 4 possible actions:
			Move right, move down, move left, & move up
	'''

	row, col = 0,0
	h_distance, v_distance = 0,0

	element_ctr = 0

	l_limit, r_limit = 0, len(matrix[0]) # The horizontal limit/width
	v_limit = len(matrix) - 1 # The vertical limit/height

	state = 1 # States can be {1,2,3, or 4} right, down, left, up

	output = []

	while element_ctr < (len(matrix) * len(matrix[0])):

		# Walk right
		if state == 1:
			if h_distance == r_limit:
				h_distance = 0
				r_limit -= 1
				col -= 1
				row += 1
				state += 1
			else:
				element_ctr += 1
				output.append(matrix[row][col])
				col += 1
				h_distance += 1

		# Walk down
		elif state == 2:
			if v_distance == v_limit:
				v_distance = 0
				v_limit -= 1
				row -= 1
				state += 1
				col -= 1
			else:
				element_ctr += 1
				output.append(matrix[row][col])
				row += 1
				v_distance += 1

		# Walk left
		elif state == 3:
			if h_distance == r_limit:
				h_distance = 0
				r_limit -= 1
				col += 1
				state += 1
				row -= 1
			else:
				element_ctr += 1
				output.append(matrix[row][col])
				col -= 1
				h_distance += 1

		# Walk up
		else:
			if v_distance == v_limit:
				v_distance = 0
				v_limit -= 1
				row += 1
				col += 1
				state = 1
			else:
				element_ctr += 1
				output.append(matrix[row][col])
				row -= 1
				v_distance += 1


	return (' ').join(map(str, output))


if __name__ == '__main__':

	matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

	print print_clockwise(matrix)