import math


def fuel_counterupper(x):
	return math.floor(int(x) / 3) - 2


if __name__ == '__main__':	
	file = open('puzzle01_input.txt', 'r')
	fuel = 0

	for x in file:
		module_fuel = fuel_counterupper(x)
		fuel += module_fuel

		while module_fuel > 0:
			module_fuel = fuel_counterupper(module_fuel)
			if module_fuel >= 0:
				fuel += module_fuel

	file.close()
	print(fuel)