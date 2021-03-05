class Node:
    def __init__(self, data: int):
        self.data = data
        self.nxt = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node: Node, data: int):
        n = Node(data)
        if node is None:
            self.head = n
        else:
            node.nxt = n
        return n

    def print_list(self):
        c = self.head
        while c is not None:
            print(c.data, end=" ")
            c = c.nxt

if __name__ == "__main__":
    n = int(input())
    linked_list = LinkedList()
    p = None
    for i in range(n):
        p = linked_list.insert(p, int(input()))
    linked_list.print_list()