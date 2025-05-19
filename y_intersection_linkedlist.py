# https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a1 = [4, 1, 8, 4, 5]
a2 = [5, 6, 1]
head1 = Node(a1[0])
head2 = Node(a2[0])
p = head1
q = head2

i = 1
while i < len(a1):
    p.next = Node(a1[i])
    p = p.next
    if i == 2:
        t = p
    i += 1

j = 1
while j < len(a2):
    q.next = Node(a2[j])
    q = q.next
    j += 1
q.next = t

p = head1
q = head2

while p != q:
    if p == None:
        p = head2
    if q == None:
        q = head1
    
    p = p.next
    q = q.next

print("The common element is:", p.data)

