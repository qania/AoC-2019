import math


def fuel_counterupper(x):
	return math.floor(int(x) / 3) - 2


if __name__ == '__main__':	
	file = open('puzzle01_input.txt', 'r')
	fuel = 0

	for x in file:
		fuel += fuel_counterupper(x)

	file.close()
	print(fuel)