def binary_search_iterative(array_list, value):
	start, end = 0, len(array_list) - 1
	while start <= end:
		mid = (start + end) // 2
		if array_list[mid] < value:
			start = mid + 1
		elif array_list[mid] > value:
			end = mid - 1
		else:
			return mid, value
	return -1


def binary_search_rec(array_list, value, start=0, end=-1):
	if end == -1:
		end = len(array_list) - 1
	if start > end:
		return -1

	mid = (start + end) // 2
	if array_list[mid] < value:
		return binary_search_rec(array_list, value, mid+1, end)
	elif array_list[mid] > value:
		return binary_search_rec(array_list, value, start, mid-1)
	else:
		return mid


def check_duplicates(array_list):
	array_list.sort()
	for i in range(len(array_list)-1):
		if array_list[i] == array_list[i+1]:
			return "Duplicate element: {}".format(array_list[i])

def check_duplicate_with_hash(array_list):
	d = {}
	for elem in array_list:
		if elem in d:
			d[elem] += 1
		else:
			d[elem] = 1
	return d

def max_count_of_element_from_list(array_list):
	d = {}
	max = 0
	for elem in array_list:
		if elem in d:
			d[elem] += 1
		else:
			d[elem] = 1
	for elem in array_list:
		if d[elem] > max:
			max = d[elem]
			max_repeated = elem
	return max_repeated, max

def bubble_sort(array_list):
	n = len(array_list)
	for i in range(n):
		for j in range(0, n-i-1):
			if array_list[j] > array_list[j+1]:
				array_list[j], array_list[j+1] = array_list[j+1], array_list[j]


def selection_sort(array_list):
	n = len(array_list)
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if array_list[j] < array_list[min_index]:
				min_index = j
		array_list[i], array_list[min_index] = array_list[min_index], array_list[i]


def insertion_sort(array_list):
	n = len(array_list)
	for i in range(1, n):
		temp = array_list[i]
		k = i
		while k>0 and temp < array_list[k-1]:
			array_list[k] = array_list[k-1]
			k -= 1
		array_list[k] = temp

def parenthesis_check(symbol_str):
	balanced = True
	st_list = []
	for symbol in symbol_str:
		if symbol in "({[":
			st_list.append(symbol)
		else:
			if not st_list:
				balanced = False
			else:
				top = st_list.pop()
				if not matches(top, symbol):
					balanced = False
	if balanced and not st_list:
		return True
	else:
		return False

def matches(top, symbol):
	opens = "({["
	closes = "]})"
	return opens.index(top) == closes.index(symbol)

