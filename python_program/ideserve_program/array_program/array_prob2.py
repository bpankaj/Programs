"""
In an array having positive integers, except for one number which occurs odd number of times,
all other numbers occur even number of times. Find the number. 
Example -  
Input : 2 5 9 1 5 1 8 2 8
Output: 9

Input : 2 3 4 3 1 4 5 1 4 2 5
Output: 4
"""

def number_occurs_at(array_list):
	data = {elem: array_list.count(elem) for elem in array_list}
	for d in data:
		if data[d] % 2 == 1:
			print(d)
			break


def number_occurs_at1(array_list):
	data = {}
	for elem in array_list:
		if elem in data:
			data[elem] += 1
		else:
			data[elem] = 1
	for d in data:
		if data[d] % 2 == 1:
			print(d)
			break