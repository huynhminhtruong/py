class Node:
	def __init__(self, value: int):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self, node: Node):
		self.root = node

	def add(self, node: Node):
		pass

	def remove(self, node: Node):
		pass

	def search(self, value: int):
		pass

	def inorder_traversal(self):
		pass

	def preorder_traversal(self):
		pass

	def postorder_traversal(self):
		pass

if __name__ == '__main__':
	n = int(input())