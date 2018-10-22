# Problem: Given a rod of length n and prices P[i] for i = 1..n, where P[i] is the
# price of a rod of length i. Find the maximum total revenue you can make by cutting
# and selling the rod(assume no cost for cutting the rod).

# Recursive call solution:
# cut a piece of length of 1: p1 + r(n-1)
# cut a piece of length of 2: p2 + r(n-2)
# ...
# cut a piece of length of n-1: p(n-1) + r1
# cut a piece of length of n: p(n)

# R(n) = max(p1 + r(n-1), p2 + r(n-2), p3 + r(n-3), ..., p(n-1) + r1, p(n))


def cutting_rod_rec(n, prices):
	"""
	n: length of the rod
	prices: list of the price 
	"""
	if n == 0:
		return 0
	max_value = 0
	for i in range(n):
		temp = prices[n - i - 1] + cutting_rod_rec(i, prices)
		if temp > max_value:
			max_value = temp
	return max_value


def cutting_rod_dp(n, prices):
	rod = [0] * (n +1)
	for i in range(1, n + 1):
		max_value = 0
		for j in range(1, i + 1):
			temp = prices[j - 1] + rod[i - j]
			if temp > max_value:
				max_value = temp
		rod[i] = max_value
	return rod[n], rod

