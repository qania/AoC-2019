import math


def fuel_counterupper(x):
	return math.floor(int(x) / 3) - 2


def get_total_fuel(x):
	fuel = 0
	module_fuel = fuel_counterupper(x)
	fuel += module_fuel

	while module_fuel > 0:
		module_fuel = fuel_counterupper(module_fuel)
		if module_fuel >= 0:
			fuel += module_fuel

	return fuel


if __name__ == '__main__':	
	file = open('puzzle01_input.txt', 'r')
	fuel = 0

	for x in file:
		fuel += get_total_fuel(x)

	file.close()
	print(fuel)


def test_fuel_counterupper():
	assert fuel_counterupper(14) == 2
	assert fuel_counterupper(1969) == 654
	assert fuel_counterupper(100756) == 33583


def test_get_total_fuel():
	assert get_total_fuel(14) == 2
	assert get_total_fuel(1969) == 966
	assert get_total_fuel(100756) == 50346