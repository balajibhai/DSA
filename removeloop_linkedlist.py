# https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = [1, 3, 4]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1

p.next = head.next
p = q = head
loop = 0

while q != None:
    if q.next != None:
        q = q.next.next
    else:
        q = q.next
    p = p.next
    
    if p == q:
        loop = 1
        break

if loop:
    p = head
    while p != q:
        p = p.next
        q = q.next
    
    while q.next != p:
        q = q.next
    q.next = None