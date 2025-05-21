class Node():
    def __init__(self,element):
        self.data=element
        self.next=None
n1=Node(105)
n2=Node(106)
n3=Node(107)
print(n1)
print(id(n1))
print(hex(id(n1)))
print(n1.data)
print(n1.next)
#connect address of n1 to n2
n1.next=n2
#connext address of n2 to n3
n2.next=n3

current=n1
while current:
    print(current.data,end=' ')
    current=current.next
