# https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# l = [5, 2, 2, 4]
l = [2, 2, 2, 2]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1

p = None
t = head
h = {}

while t != None:
    if t.data in h:
        p.next = t.next
        t.next = None
        if p != None:
            t = p.next
    else:
        h[t.data] = 1
        p = t
        t = t.next
    

p = head
while p != None:
    print(p.data)
    p = p.next