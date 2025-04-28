# https://www.geeksforgeeks.org/problems/reorder-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

arr = [1, 2]
l = len(arr)
head = Node(1)
p = head

for i in range(1, l):
    p.next = Node(arr[i])
    p = p.next

sp = head
fp = head

while True:
    fp = fp.next.next
    sp = sp.next
    if fp.next == None or fp.next.next == None:
        break

# sh means second_half of the linked_list
sh = sp.next
sp.next = None

# reversing the second_half of the linked_list
t1 = sh

if t1.next != None:
    t2 = t1.next
    t = t2.next
    t1.next = None

    while t2 != None:
        t2.next = t1
        t1 = t2
        t2 = t
        if t != None:
            t = t.next

# Now t1 is the head of the reversed part of the second_half
p = head
index = 1
temp2 = t1

while p != None:
    index += 1
    if index % 2 == 0:
        temp1 = p.next
        p.next = temp2
    else:
        temp2 = p.next
        p.next = temp1
    p = p.next


p = head

while p != None:
    print(p.data, end = " ")
    p = p.next
print()