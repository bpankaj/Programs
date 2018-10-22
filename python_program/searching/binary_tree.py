    """DFS: “is an algorithm for traversing or searching tree data structure.
    One starts at the root and explores as far as possible along each branch before backtracking.” — Wikipedia
    BFS: “is an algorithm for traversing or searching tree data structure.
    It starts at the tree root and explores the neighbor nodes first, before moving to the next level neighbors.” — Wikipedia"""

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None


	def insert_left(self, value):
		if self.left_child is None:
			self.left_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.left_child = self.left_child
			self.left_child = new_node


	def insert_right(self, value):
		if self.right_child is None:
			self.right_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.right_child = self.right_child
			self.right_child = new_node


# DFS: we have pre-order, in-order, post-order traversal

	def pre_order(self):
		# Root Node
		print(self.value)

		# Left Node
		if self.left_child:
			print(self.left_child.pre_order())

		# Right Node
		if self.right_child:
			print(self.right_child.pre_order())


	def in_order(self):
		if self.left_child:
			print(self.left_child.in_order())

		print(self.value)

		if self.right_child:
			print(self.right_child.in_order())


	def post_order(self):
		if self.right_child:
			print(self.right_child.post_order())
		if self.left_child:
			print(self.left_child.post_order())
		print(self.value)
