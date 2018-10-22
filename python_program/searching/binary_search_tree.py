class Node:
	def __init__(self, value):
		self.value = value
		self.leftchild = None
		self.rightchild = None

	def insert_data(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.leftchild:
				return self.leftchild.insert_data(data)
			else:
				self.leftchild = Node(data)
				return True
		else:
			if self.rightchild:
				return self.rightchild.insert_data(data)
			else:
				self.rightchild = Node(data)

	def find_data(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.leftchild:
				return self.leftchild.find_data(data)
			else:
				return False
		else:
			if self.rightchild:
				return self.rightchild.find_data(data)
			else:
				return False

	def preorder(self):
		if self:
			print(str(self.value))
			if self.leftchild:
				self.leftchild.preorder()
			if self.rightchild:
				self.rightchild.preorder()

	def postorder(self):
		if self:
			if self.leftchild:
				self.leftchild.postorder()
			if self.rightchild:
				self.rightchild.postorder()
			print(str(self.value))

	def inorder(self):
		if self:
			if self.leftchild:
				self.leftchild.inorder()
			print(str(self.value))
			if self.rightchild:
				self.rightchild.inorder()

# References: https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert_data(self, data):
		if self.root:
			return self.root.insert_data(data)
		else:
			self.root = Node(data)
			return True

	def find_data(self, data):
		if self.root:
			return self.root.find_data(data)
		else:
			return False

	def preorder(self):
		print("Pre-Order Traversal")
		self.root.preorder()

	def postorder(self):
		print("Post-Order Traversal")
		self.root.postorder()

	def inorder(self):
		print("In-Order Traversal")
		self.root.inorder()


class BinarySearchTreeNew:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
    	if value <= self.value and self.left_child:
    		self.left_child.insert_node(value)
    	elif value <= self.value:
    		self.left_child = BinarySearchTreeNew(value)
    	elif value > self.value and self.right_child:
    		self.right_child.insert_node(value)
    	else:
    		self.right_child = BinarySearchTreeNew(value)

    # Search the value
    def find_node(self, value):
        if value < self.value and self.left_child:
        	return self.left_child.find_node(value)
        if value > self.value and self.right_child:
        	return self.right_child.find_node(value)
        return value == self.value

    # Traversal
    def pre_order(self):
    	print(self.value)
    	if self.left_child:
    		print(self.left_child.pre_order())
    	if self.right_child:
    		print(self.right_child.pre_order())

    def in_order(self):
    	if self.left_child:
    		print(self.left_child.in_order())
    	print(self.value)
    	if self.right_child:
    		print(self.right_child.in_order())

    def post_order(self):
    	if self.left_child:
    		print(self.left_child.post_order())
    	if self.right_child:
    		print(self.right_child.post_order())
    	print(self.value)

    def remove_node(self, value, parent):
    	if value < self.value and self.left_child:
    		return self.left_child.remove_node(value, self)
    	elif value < self.value:
    		return False
    	elif value > self.value and self.right_child:
    		return self.right_child.remove_node(value, self)
    	elif value > self.value:
    		return False
    	else:
    		if self.left_child is None and self.right_child is None and self == parent.left_child:
    			parent.left_child = None
    			self.clear_node()
    		elif self.left_child is None and self.right_child is None and self == parent.right_child:
    			parent.right_child = None
    			self.clear_node()
    		elif self.left_child and self.right_child is None and self == parent.left_child:
    			parent.left_child = self.left_child
    			self.clear_node()
    		elif self.left_child and self.right_child is None and self == parent.right_child:
    			parent.right_child = self.left_child
    			self.clear_node()
    		elif self.right_child and self.left_child is None and self == parent.left_child:
    			parent.left_child = self.right_child
    			self.clear_node()
    		elif self.right_child and self.left_child is None and self == parent.right_child:
    			parent.right_child = self.right_child
    			self.clear_node()
    		else:
    			self.value = self.right_child.find_minimum_value()
    			self.right_child.remove_node(self.value, self)
    	return True
    
    def clear_node(self):
    	self.value = None
    	self.left_child = None
    	self.right_child = None

    def find_minimum_value(self):
    	if self.left_child:
    		return self.left_child.find_minimum_value()
    	else:
    		return self.value

