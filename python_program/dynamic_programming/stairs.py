# Problem 1: You can climb 1 or 2 stairs with one step.
# How many different ways can you climb n stairs.

# Recursive call

def stairs_rec(num):
	if num == 1:
		return 1
	if num == 2:
		return 2

	return stairs_rec(num - 1) + stairs_rec(num - 2)

# stairs(40) it took more than 40 sec  and for 100 it took more than 1 hour.


# Dynamic programming

def stairs_dp(num):
	st = [0] * num
	st[0], st[1] = 1, 2

	for i in range(2, num):
		st[i] = st[i - 1] + st[i - 2]
	return st[num - 1]


# Problem 2: You can climb 1 or 2 or 3 stairs with one step.
# How many different ways can you climb n stairs.


def stairs_rec1(num):
	if num == 1:
		return 1
	if num == 2:
		return 2
	if num == 3:
		return 3

	return stairs_rec1(num - 1) + stairs_rec1(num - 2) + stairs_rec1(num - 3)

def stairs_dp1(num):
	st = [0] * num
	st[0], st[1], st[2] = 1, 2, 3

	for i in range(3, num):
		st[i] = st[i - 1] + st[i - 2] + st[i - 3]
	return st[num - 1]


