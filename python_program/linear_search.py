def unordered_linear_search(numberlist, value):
    for i in range(len(numberlist)):
	if numberlist[i] == value:
	    return i
    return -1

def ordered_linear_search(numberlist, value):
	for i in range(len(numberlist)):
		if numberlist[i] == value:
			return i
		elif numberlist[i] > value:
			return -1


