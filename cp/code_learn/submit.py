import math
from operator import itemgetter

class Node:
    def __init__(self, data: int):
        self.data = data
        self.nxt = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, node: Node, data: int):
        n = Node(data)
        if node is None:
            self.head = n
        else:
            node.nxt = n
        self.size += 1
        self.tail = n
        return n

    def insert(self, data: int, position: int):
        node = Node(data)
        c = self.head
        if position == 0:
            node.nxt = self.head
            self.head = node
        elif self.size <= position:
            self.tail.nxt = node
            self.tail = self.tail.nxt
        else:
            while c.nxt is not None and position > 1:
                c = c.nxt
                position -= 1
            node.nxt = c.nxt
            c.nxt = node
        self.size += 1

    def append(self, data: int):
        node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = node
        else:
            c = self.head
            while c.next is not None:
                c = c.next
            c.next = node
    
    def delete(self, position: int):
        c = self.head
        if position == 0:
            self.head = self.head.nxt
        else:
            while c.nxt is not None and position > 1:
                c = c.nxt
                position -= 1
            deleted_node = c.nxt
            c.nxt = deleted_node.nxt
        return self.head

    def print_list(self):
        c = self.head
        while c is not None:
            print(c.data, end=" ")
            c = c.nxt

if __name__ == "__main__":
    n = int(input())
    linkedlist = LinkedList()
    p = None
    for i in range(n):
        p = linkedlist.insert(p, int(input()))
    k = int(input())
    x = int(input())
    linkedlist.insert_at_position(x, k)
    linkedlist.print_list()