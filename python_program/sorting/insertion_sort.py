def insertion_sort(list_arr):
	for i in range(1, len(list_arr)):
		key = list_arr[i]
		j = i - 1
		while j > = 0 and key < list_arr[j]:
			list_arr[j+1] = list_arr[j]
			j -= 1
		list_arr[j+1] = key