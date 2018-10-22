# Top Down approach(Memoization)

def fib_top_down(n, lookup_list):
	if n == 0 or n == 1:
		lookup_list[n] = n
	if lookup_list[n] is None:
		lookup_list[n] = fib_top_down(n - 1, lookup_list) + fib_top_down(n - 2, lookup_list)
	return lookup_list[n]

# n = 10
# lookup_list = [None] * (n + 1)
# fib(n, lookup_list) ==> O/P: 55
# print lookup_list
# O/P: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Bottom up approach(Tabulization)

def fib_bottom_up(n):
	fi = [0] * (n + 1)
	fi[0] = 1
	for i in xrange(2, n + 1):
		fi[i] = fi[i - 1] + fi[i - 2]
	return fi

# fib(10)
# O/P: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]