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

def reverse(head):
    t1 = head
    t2 = t1.next
    t1.next = None

    while t2 != None:
        t = t2.next
        t2.next = t1
        t1 = t2
        t2 = t
    
    return t1

t1 = reverse(head)
while t1 != None:
    print(t1.data)
    t1 = t1.next

