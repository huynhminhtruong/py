class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST:

	def __init__(self):
		self.root = None
		self.__level = 0

	@property
	def level(self):
		return self.__level

	@level.setter
	def level(self, value: int):
		self.__level += value

	def add(self, node: Node, data: int):
		if self.root is None:
			self.root = Node(data)
		else:
			if node.value > data:
				if node.left: self.add(node.left, data)
				else: node.left = Node(data)
			else:
				if node.right: self.add(node.right, data)
				else: node.right = Node(data)

	def inorder_traversal(self, node: Node):

		# Recursive left node
		# Access root node
		# Recursive right node

		if node:
			self.inorder_traversal(node.left)
			print(node.value)
			self.inorder_traversal(node.right)

	def preorder_traversal(self, node: Node):

		# Access root node
		# Recursive left node
		# Recursive right node

		if node:
			print(node.value)
			self.preorder_traversal(node.left)
			self.preorder_traversal(node.right)

	def postorder_traversal(self, node: Node):

		# Recursive left node
		# Recursive right node
		# Access root node

		if node:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print(node.value)

	def count_leaf(self, node: Node):
		if node is None: return 0
		if node.left is None and node.right is None: return 1
		return self.count_leaf(node.left) + self.count_leaf(node.right)

	def tree_level(self, node: Node):
		if node is None: return -1
		return 1 + max(self.tree_level(node.left), self.tree_level(node.right))

if __name__ == '__main__':
	n = int(input())
	bst, node = BST(), None

	for i in range(n):
		node = bst.add(bst.root, int(input()))
	print(bst.tree_level(bst.root))