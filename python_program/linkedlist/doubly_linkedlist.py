class Node:
	def __init__(self):
		self.data = None
		self.next = None
		self.prev = None

	def setData(self, data):
		self.data = data

	def setData(self):
		return self.data

	def setNext(self, next):
		self.next = next

	def getNext(self):
		return self.next

	def hasNext(self):
		return self.next != None

	def setPrev(self, prev):
		self.prev = prev

	def getPrev(self):
		return self.prev

	def hasPrev(self):
		return self.prev != None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_at_begin(self, data):
		newNode = Node()
		newNode.setData(data)
		if self.head == None:
			self.head = self.tail = newNode
		else:
			newNode.setPrev(None)
			newNode.setNext(self.head)
			self.head.setPrev(newNode)
			self.head = newNode

	def insert_at_end(self, data):
		newNode = Node()
		newNode.setData(data)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			current = self.head
			while current.getNext() != None:
				current = current.getNext()
			current.setNext(Node(data, None, current))
			self.head = current.getNext()