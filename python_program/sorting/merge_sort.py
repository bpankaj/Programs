def merge_sort(list_arr):
	if len(list_arr) <= 1:
		return list_arr
	middle = int(len(list_arr) / 2)
	left = merge_sort(list_arr[:middle])
	right = merge_sort(list_arr[middle:])
	return merge(left, right)

def merge(first, last):
	result = []
	i = j = 0
	while i < len(first) and j < len(last):
		if first[i] <= last[j]:
			result.append(first[i])
			i += 1
		else:
			result.append(last[j])
			j += 1
	result += first[i:]
	result += last[j:]
	return result
