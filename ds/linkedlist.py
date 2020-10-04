class SingleNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class DoubleNode:
	def __init__(self, data):
		self.previous = None
		self.next = None
		self.data = data

class LinkedList:
	def __init__(self):
		self.__head = None
		self.__tail = None

	def set_head(self, node: SingleNode = None):
		self.__head = node

	def get_head(self):
		return self.__head

	def set_tail(self, node: SingleNode = None):
		self.__tail = node

	def get_tail(self):
		return self.__tail

	def push(self, node: SingleNode):
		pass

	def append(self, node: SingleNode):
		pass

	def insert(self, node: SingleNode):
		if self.get_head() is None:
			self.set_head(node)
		else:
			current_node = self.get_head()
			while (current_node.next != None):
				current_node = current_node.next
			current_node.next = node
			self.set_tail(current_node.next)

	def delete(self, node: SingleNode):
		prev_node, current_node = self.search_node(node)

		# Delete head
		if (prev_node == None and current_node != None):
			self.set_head(current_node.next)
			current_node = None
			return current_node

		# Delete tail
		if (prev_node != None and current_node == None):
			prev_node.next = None
			self.set_tail(prev_node)
			return current_node

		# Delete node between head and tail
		if (prev_node != None and current_node != None):
			prev_node.next = current_node.next
			return current_node

		return None

	def search(self, node: SingleNode):
		if self.get_head() is not None:
			prev_node = None
			current_node = self.get_head()
			while (current_node != None and current_node.data != node.data):
				prev_node = current_node
				current_node = current_node.next
			if (current_node is not None):
				return prev_node, current_node
		return None, None

	def print_linked_list(self):
		current_node = self.get_head()
		while (current_node != None):
			print(current_node.data)
			current_node = current_node.next

if __name__ == '__main__':
	n = int(input())
	a = [int(x) for x in input().split()]
	ll = LinkedList()

	for _ in range(0, n):
		node = SingleNode(a[_])
		ll.insert_node(node)

	ll.print_linked_list()
	print("Deleting a node: ")
	data = int(input())
	print("Alter deleting operator is executed: ")
	del_node = Node(data)
	ll.delete_node(del_node)
	ll.print_linked_list()

