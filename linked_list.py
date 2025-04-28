# https://www.geeksforgeeks.org/problems/print-linked-list-elements/1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(3)
c = Node(4)
a.next = b
b.next = c
c.next = None
p = a
n = 3
for i in range(n):
    print(p.data)
    p = p.next