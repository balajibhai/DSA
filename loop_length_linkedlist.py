# https://www.geeksforgeeks.org/problems/find-length-of-loop/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = [1, 2, 3, 4, 5]
head = Node(l[0])
p = head
i = 1

while i < len(l):
    p.next = Node(l[i])
    p = p.next
    i += 1

p.next = head
p = head
q = head
count = 0
loop = 0

if head.next == None:
    print(loop)
else:
    while q != None:
        p = p.next
        if q.next != None:
            q = q.next.next
        else:
            q = q.next
        if p == q:
            loop = 1    
            break

    if loop:
        while True:
            q = q.next
            count += 1
            if p == q:
                break
        print(count)
    else:
        print(loop)