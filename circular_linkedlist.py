class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
n1=Node(1122)
n2=Node(2233)
n3=Node(3344)
n4=Node(4455)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n1
current=n1
while current.next!=n1:
    print(current.data,end='-> ')
    current=current.next
print(current.data,end='->')