class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST:

	def __init__(self):
		self.root = None

	def add(self, node: Node, data: int):
		if self.root is None:
			self.root = Node(data)
		else:
			if node.value >= data:
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

if __name__ == '__main__':
	n = int(input())
	bst, node = BST(), None

	for i in range(n):
		node = bst.add(bst.root, int(input()))
	print("Traversal: ")
	bst.inorder_traversal(bst.root)