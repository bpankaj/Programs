def bubble_sort(list_arr):
	n = len(list_arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if list_arr[j] > list_arr[j+1]:
				list_arr[j], list_arr[j+1] = list_arr[j+1], list_arr[j]

# Above program have complexity O(n2).

def bubble_sort1(list_arr):
	n = len(list_arr)
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if list_arr[j] > list_arr[j+1]:
				list_arr[j], list_arr[j+1] = list_arr[j+1], list_arr[j]
				swapped = True
		if not swapped:
			break