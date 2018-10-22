class Node:
	def __init__(self):
		self.data = None
		self.next = None

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self, next):
		self.next = next

	def getNext(self):
		return self.next

	def hasNext(self):
		return self.next != None


class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None

	def insert_at_beginning(self, data):
		newNode = Node()
		newNode.setData(data)
		if self.length == 0:
			self.head = newNode
		else:
			newNode.setNext(self.head)
			self.head = newNode
		self.length += 1

	def list_length(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			print current.getData()
			current = current.getNext()
		return count

	def insert_at_end(self, data):
		newNode = Node()
		newNode.setData(data)
		current = self.head
		while current.getNext() != None:
			current = current.getNext()
		current.setNext(newNode)
		self.length += 1

	def insert_at_position(self, pos, data):
		if pos > self.length or pos < 0:
			return None
		else:
			if pos == 0:
				self.insert_at_beginning(data)
			else:
				if pos == self.length:
					self.insert_at_end(data)
				else:
					newNode = Node()
					newNode.setData(data)
					count = 0
					current = self.head
					while count < pos - 1:
						count += 1
						current = current.getNext()
					newNode.setNext(current.getNext())
					current.setNext(newNode)
					self.length += 1

	def reverse_list(self):
		last = None
		current = self.head
		while current is not None:
			nextNode = current.getNext()
			current.setNext(last)
			last = current
			current = nextNode
		self.head = last

	def reverse_list1(self):
		new_head = None
		while self.head:
			self.head.next, self.head, new_head = new_head, self.head.next, self.head # look Ma, no temp vars!
			print new_head.getData()
		return new_head

	def delete_at_first(self):
		if self.length == 0:
			print "List is empty"
		else:
			self.head = self.head.getNext()
			self.length -= 1

	def delete_at_last(self):
		if self.length == 0:
			print "List is empty."
		else:
			currentNode = self.head
			previousNode = self.head
			while currentNode.getNext != None:
				previousNode = currentNode
				currentNode = currentNode.getNext()
			previousNode.setNext(None)
			self.length -= 1

	def delete_at_pos(self, pos):
		count = 0
		currentNode = self.head
		previousNode = self.head
		if pos > self.length or pos < 0:
			print "Please enter proper position"
		else:
			while currentNode.next != None or count < pos:
				count += 1
				if count == pos:
					previousNode.next = currentNode.next
					self.length -= 1
					return
				else:
					previousNode = currentNode
					currentNode = currentNode.next
