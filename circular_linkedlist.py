# https://www.geeksforgeeks.org/problems/circular-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = [2, 4, 6, 7, 5]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1

p.next = head

p = head
t = head
flag = False

while p != None:
    p = p.next
    if p == t:
        flag = True
        break

print(flag)