class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linkedlist(arr):
    head = Node(arr[0])
    p = head
    i = 1

    while i < len(arr):
        p.next = Node(arr[i])
        p = p.next
        i += 1
    
    return head

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

def print_linked_list(statement, t):
    print(statement)
    while t != None:
        print(t.data, end=" ")
        t = t.next
    print()

# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8]

# l1 = [4, 5]
# l2 = [3, 4, 5]

l1 = [0, 0, 6, 3]
l2 = [0, 7]
res_arr = []
h1 = create_linkedlist(l1)
h2 = create_linkedlist(l2)
t1 = reverse(h1)
print_linked_list("printing reverse of first linked_list:", t1)
t2 = reverse(h2)
print_linked_list("printing reverse of second linked_list:", t2)
carry = 0

while t1 != None and t2 != None:
    res = t1.data + t2.data + carry
    ones_digit = res % 10
    carry = res // 10
    res_arr.append(ones_digit)
    t1 = t1.next
    t2 = t2.next

if t1 != None:
    t = t1
else:
    t = t2

while t != None:
    res = t.data + carry
    ones_digit = res % 10
    carry = res // 10
    res_arr.append(ones_digit)
    t = t.next

print("Forward addition of both reversed linked_lists:", res_arr)
req_str = ""

for i in res_arr:
    req_str += str(i)

req_num = int(req_str[::-1])
print("reversed list and concatenated to a number:", req_num)
req_str = str(req_num)
req_arr = []
print("converting number to list...")

for i in req_str:
    req_arr.append(int(i))

print(req_arr)
res_head = create_linkedlist(req_arr)
print_linked_list("printing the final linked_list:", res_head)
