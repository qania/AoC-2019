def intcode(values):
	pos = 0
	
	for i in range(len(values)):
		opcode = values[pos]

		if opcode == 99:
			break

		in_pos1 = values[pos + 1]
		in_pos2 = values[pos + 2]
		out_pos = values[pos + 3]

		if opcode == 1:
			values[out_pos] = values[in_pos1] + values[in_pos2]
			pos += 4
		elif opcode == 2:
			values[out_pos] = values[in_pos1] * values[in_pos2]
			pos += 4

	return values


if __name__ == '__main__':
	file = open('input.txt', 'r')
	codes = file.read().split(',')
	file.close()

	values = [int(value) for value in codes]

	print(intcode(values))


def test_intcode():
	assert intcode([1,0,0,0,99]) == [2,0,0,0,99]
	assert intcode([2,3,0,3,99]) == [2,3,0,6,99]
	assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
	assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
	assert intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]