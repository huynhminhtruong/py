class Node:
	def __init__(self, value: int):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self, node: Node):
		self.root = node

	def add_node(self, node: Node):
		pass

	def remove_node(self, node: Node):
		pass

	def search_node(self, value: int):
		pass

	def inorder_traversal(self):
		pass

	def preorder_traversal(self):
		pass

	def postorder_traversal(self):
		pass

if __name__ == '__main__':
	n = int(input())