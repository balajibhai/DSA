class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = [2, 2, 2, 2]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1