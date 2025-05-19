# https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# l = [2, 2, 4, 5]
l = [2, 2, 2, 2, 2]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1

p = head

# To print if needed
# i = 1
# while p != None:
#     print(p.data)
#     p = p.next
t = p.next

while t != None:
    if p.data == t.data:
        p.next = t.next
        t.next = None
    else:
        p = p.next
    t = p.next

p = head
while p != None:
    print(p.data)
    p = p.next
