# Iterative Binary Search Algorithm

def binary_search_iterative(numberlist, value):
	low = 0
	high = len(numberlist) - 1
	while low <= high:
		mid = (low + high) // 2
		if numberlist[mid] > value:
			high = mid - 1
		elif numberlist[mid] < value:
			low = mid + 1
		else:
			return mid
	return -1

# Recursive binary search Algorithm
def binary_search_recursive(numberlist, value, low=0, high=-1):
	if not numberlist:
		return -1
	if high == -1:
		high = len(numberlist) - 1
	if low == high:
		if numberlist[low] == value:
			return low
		else:
			return -1
	mid = low + (high - low) // 2
	if numberlist[mid] > value:
		return binary_search_recursive(numberlist, value, low, mid - 1)
	elif numberlist[mid] < value:
		return binary_search_recursive(numberlist, value, mid + 1, high)
	else:
		return mid
