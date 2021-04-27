# code_learn

class Node:
    def __init__(self, data: int):
        self.data = data
        self.nxt = None

class DoublyNode:
    def __init__(self, data: int):
        self.data = data
        self.nxt = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_1(self, node: Node, data: int):
        n = Node(data)
        if node is None:
            self.head = n
        else:
            node.nxt = n
        return n
    
    def insert_2(self, node: DoublyNode, data: int):
        n = DoublyNode(data)
        if node is None:
            self.head = n
        else:
            node.nxt = n
            n.prev = node
        return n
    
    def insert_3(self, x: int, k: int):
        node = self.head
        n = DoublyNode(x)
        if not k:
            n.nxt = node
            node.prev = n
            self.head = n
        else:
            k -= 1
            while k > 0:
                node = node.nxt
                k -= 1
            if node.nxt is None:
                node.nxt = n
            else:
                n.nxt = node.nxt
                n.prev = node
                node.nxt.prev = n
                node.nxt = n
        return None
    
    def delete(self, k: int):
        node = prev = self.head

        if not k:
            self.head = self.head.nxt
            return None
        while k > 0:
            prev = node
            node = node.nxt
            k -= 1
        prev.nxt = node.nxt
        return None
    
    def delete_2(self, k: int):
        node = self.head
        if not k:
            self.head = node.nxt
            node.prev = None
        else:
            while not node.nxt is None and k > 0:
                node = node.nxt
                k -= 1
            node.prev.nxt = node.nxt
            if not node.nxt is None:node.nxt.prev = node.prev
        return None
    
    def get_node_at_position(self, k: int):
        node = self.head

        while k > 0:
            node = node.nxt
            k -= 1
        return self.get_value(node)
    
    def get_value(self, node: Node):
        return node.data

    def change_value(self, a: int, b: int):
        node = self.head
        while not node is None:
            if node.data == a:
                node.data = b
            node = node.nxt
        return None
    
    def delete_greater_than_k(self, k: int):
        node = prev = self.head
        cnt = 0

        while k > 0:
            node = node.nxt
            k -= 1

        k = node.data
        node = prev

        while not node is None:
            if node.data > k:
                if not cnt:self.head = node.nxt
                else:prev.nxt = node.nxt
            else:
                prev = node
                cnt += 1
            node = node.nxt
        return None

    def __str__(self):
        c = self.head
        s = ""
        while c is not None:
            s += str(c.data) + " "
            c = c.nxt
        return s
    
    def print(self):
        node = self.head
        while not node.nxt is None:
            print(node.data, end=" ")
            node = node.nxt
        while not node is None:
            print(node.data, end=" ")
            node = node.prev

class CircularLinkedList:

    # Could use SingleNode and DoublyNode for implementation
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node: Node, data: int):
        n = Node(data)

        if self.head is None: self.head = n
        else: node.nxt = n

        self.tail = n
        self.tail.nxt = self.head

        return n

    def print(self, k: int, n: int):
        node = self.head
        while k > 0:
            node = node.nxt
            k -= 1
        while k < n:
            print(node.data, end=" ")
            node = node.nxt
            k += 1

    def __str__(self):
        pass

if __name__ == "__main__":
    n = int(input())
    llist = CircularLinkedList()
    p = None
    for i in range(n):
        p = llist.insert(p, int(input()))
    k = int(input())
    llist.print(k, n)