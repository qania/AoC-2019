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


def initialise_memory(file):
	fp = open(file, 'r')
	codes = fp.read().split(',')
	fp.close()

	return [int(value) for value in codes]


def find_noun_verb(values):
	for i in range(99):
		for j in range(99):
			values[1] = i
			values[2] = j

			result = intcode(values)

			if result[0] != 19690720:
				values = initialise_memory('origin-input.txt')
			else:
				return values


if __name__ == '__main__':
	memory = initialise_memory('origin-input.txt')
	result = find_noun_verb(memory)

	print(f'noun: {result[1]}, verb: {result[2]}')
	print(100 * result[1] + result[2])