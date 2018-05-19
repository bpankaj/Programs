def selection_sort(list_arr):
	for i in range(len(list_arr)):
		min_index = i
		for j in range(i+1, len(list_arr)):
			if list_arr[min_index] > list_arr[j]:
				min_index = j
		list_arr[i], list_arr[min_index] = list_arr[min_index], list_arr[i]