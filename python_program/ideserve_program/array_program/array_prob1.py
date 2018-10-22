""" Given a sorted array of integers containing duplicates, write a program which returns the last index
of an element.

Example:
Input:
array = [0, 1, 2, 2, 4, 5, 5, 5, 8];
num = 5;
Output: 
Element 5 found at index 7
"""

def last_index(array_list, num):
	for i in range(len(array_list) - 1, -1, -1):
		if array_list[i] == num:
			print("Num: {} found at index: {}".format(num, i))
			break


"""
Given a sorted array of integers containing duplicates, write a program which returns the first index
of an element.

Example:
Input:
array = [0, 1, 2, 2, 4, 5, 5, 5, 8];
num = 5;
Output: 
Element 5 found at index 5
"""

def first_index(array_list, num):
	for i in range(len(array_list)):
		if array_list[i] == num:
			print("Num: {} found at index: {}".format(num, i))
			break