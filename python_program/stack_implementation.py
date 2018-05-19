class Stack(object):
	"""
	Stack implementation with list
	"""
	def __init__(self):
		self.stack_list = []

	def is_empty(self):
		return self.stack_list == []

	def push(self, data):
		self.stack_list.append(data)

	def pop(self):
		return self.stack_list.pop()

	def top(self):
		if not self.stack_list
			return "Stack is empty"
		return self.stack_list[-1]

class Node(object):
	"""
	Creating Node for stack
	"""
	def __init__(self):
		self.data = None
		self.next = None

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_next(self, next):
		self.next = next

	def get_next(self):
		return self.next


class StackNode(object):
	"""
	Stack implementation without using list
	"""
	def __init__(self):
		self.head = None
		
	def push(self, data):
		newNode = Node()
		newNode.set_data(data)
		newNode.set_next(self.head)
		self.head = newNode

	def pop(self):
		if not self.head:
			return "Stack is empty"
		temp = self.head.get_data()
		self.head = self.head.get_next()
		return temp

	def top(self):
		if not self.head:
			return "Stack is empty"
		return self.head.get_data()


# Program to check paranthesis is matching or not

def paranthesis_check(symbol_str):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_str) and balanced:
		symbol = symbol_str[index]
		if symbol in "({[":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1
	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(top, symbol):
	opens = "({["
	closes = "]})"
	return opens.index(top) == closes.index(symbol)

# Program to convert decimal to binary, octal, hex

def base_convert(decimal_number, base):
	digits = "0123456789ABCDEF"
	st = Stack()

	while decimal_number > 0:
		rem = decimal_number % base
		st.push(rem)
		decimal_number = decimal_number // base

	new_string = ''
	while not st.is_empty():
		new_string = new_string + digits[st.pop()]
	return new_string
