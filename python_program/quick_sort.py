def partition(list_arr, first, last):
	i = first - 1
	pivot = list_arr[last]
	for j in range(first, last):
		if list_arr[j] <= pivot:
			i += 1
			list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
	list_arr[i+1], list_arr[last] = list_arr[last], list_arr[i+1]
	return (i+1)

def quick_sort(list_arr, first, last):
	if first < last:
		pi = partition(list_arr, first, last)
		quick_sort(list_arr, first, pi-1)
		quick_sort(list_arr, pi+1, last)

#list_arr = [9, 0, -3, 8, 1, 3, 2, 10]
#first, last = 0, len(list_arr) - 1