# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = [1, 2, 2, 1, 2, 0, 2, 2]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1

h = {}
p = head

while p != None:
    if p.data in h:
        h[p.data] += 1
    else:
        h[p.data] = 1
    p = p.next

p = head

while p != None:
    if 0 in h and h[0] > 0:
        p.data = 0
    elif 1 in h and h[1] > 0:
        p.data = 1
    else:
        p.data = 2
        
    h[p.data] -= 1
    p = p.next

p = head
while p != None:
    print(p.data)
    p = p.next