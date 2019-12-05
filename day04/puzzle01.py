def check_dupes(num_list):
	if len(num_list) == len(set(num_list)):
		return False
	else:
		return True


def check_increase(num_list):
	if num_list == sorted(num_list):
		return True
	else:
		return False


def check_pass_criteria(num_list):
	if not check_dupes(num_list):
		return False
	else:
		if check_increase(num_list):
			return True

	return False


if __name__ == '__main__':
	start = 240920
	stop = 789857
	step = 1
	pass_count = 0

	for num in range(start, stop, step):
		digits = [int(x) for x in str(num)]
		if check_pass_criteria(digits):
			pass_count += 1

	print(pass_count)


def test_check_dupes():
	assert check_dupes([1,1,2,3,4]) == True
	assert check_dupes([1,2,3,4]) == False


def test_check_increase():
	assert check_increase([1, 2, 3, 4, 5]) == True
	assert check_increase([1, 2, 0, 5]) == False
	assert check_increase([1, 1, 2, 3, 4]) == True
	assert check_increase([1, 1, 0, 3]) == False
	assert check_increase([1, 1, 1, 1]) == True


def test_check_pass_criteria():
	assert check_pass_criteria([1,1,1,1,1,1]) == True
	assert check_pass_criteria([2,2,3,4,5,0]) == False
	assert check_pass_criteria([1,2,3,7,8,9]) == False