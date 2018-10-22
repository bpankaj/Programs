# Catalon numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862

def catalan_numbers(num):
	if num <= 1:
		return num
	result = 0
	for i in range(num):
		result += catalan_numbers(i) * catalan_numbers(num - i - 1)
	result