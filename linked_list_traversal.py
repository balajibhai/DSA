# https://www.geeksforgeeks.org/problems/print-linked-list-elements/1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = [1,2,3,4,5]
head = Node(n[0])
p = head

for i in n:
    p.next = Node(i)
    p = p.next

p = head

while p.next != None:
    p = p.next
    print(p.data)
