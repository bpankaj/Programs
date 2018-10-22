# Given a nested list of integers write a function which returns sum of all its elements weighed by its depth.
list1 = [5, [7,8, [4, 9] , 6], 2] # => 5*1 + 7*2 + 8*2 + 4*3 + 9*3 + 6*2 + 2*1

def nested_sum(list1):
	def nested_sum_wrapper(list1, depth):
		result = 0
		for l in list1:
			if len(str(l)) == 1 and str(l):
				result += int(l) * depth
			else:
				result += nested_sum_wrapper(l if isinstance(l, list) else [], depth + 1)
		return result
	return nested_sum_wrapper(list1, 1)


import itertools
def longest_palindrome(s):
    lp, lp_len = '', 0
    for start, stop in itertools.combinations(range(len(s)+1), 2):
        ss = s[start:stop]  # substring
        if (len(ss) > lp_len) and (ss == ss[::-1]):
            lp, lp_len = ss, len(ss)
    return lp

def triangle_right(n):
    for i in range(1, n+1):
        print ('#'*i).rjust(n, ' ')


def triangle_left(n):
    for i in range(1, n+1):
        print ('#'*i).rjust(n, ' ')

def merge_sort(list_arr):
	if len(list_arr) <= 1:
		return list_arr
	middle = list_arr // 2
	left = merge_sort(list_arr[:middle])
	right = merge_sort(list_arr[middle:])
	merge(left, right)

def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        substring_map = {}
        start = 0
        for i in range(len(s)):
            position = substring_map.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                longest = max(length, longest)
            substring_map[s[i]] = i
        longest = max(len(s) - start, longest)
        return longest

def lengthOfLongestSubstring(s):
    checklist = {}
    starting_index_of_current_substring = 0
    length_of_longest_substring = 0
    for i, v in enumerate(s):
        if v in checklist:
            starting_index_of_current_substring = max(starting_index_of_current_substring, checklist[v] + 1)
        checklist[v] = i
        length_of_longest_substring = max(length_of_longest_substring, i - starting_index_of_current_substring + 1)
    return length_of_longest_substring

class Solution1:
	def lengthOfLongestSubstring(self, s):
		seen = []
		mx = 0
		ctr = 0
		for ch in s:
			if ch not in seen:
				ctr += 1
			else:
				i = seen.index(ch)
				seen = seen[i+1:]
			mx = ctr if ctr > mx else mx
			ctr = len(seen) + 1
			seen.append(ch)
		return ctr if ctr > mx else mx


# Transpose of matrix by using list comprehension

#[[row[i] for row in l]for i in range(len(l[0]))]


from functools import wraps
import logging
import sys
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def logger_func(func):
	@wraps(func)
	def wrapper_logger_func(*args, **kwargs):
		logger.info("Calling function: {} with arguments- args: {}, kwargs: {}".format(func.__name__, args, kwargs))
		value = func(*args, **kwargs)
		logger.info("Called function: {} values: {}".format(func.__name__, value))
		return value
	return wrapper_logger_func


@logger_func
def add1(a, b):
	return a + b

