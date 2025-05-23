# https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

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

if head.next == None:
    print(False)
else:
    p = head
    q = head
    loop = False

    while q != None:
        p = p.next
        if q.next != None:
            q = q.next.next
        else:
            q = q.next
        if p == q:
            loop = True
            break

    print(loop)