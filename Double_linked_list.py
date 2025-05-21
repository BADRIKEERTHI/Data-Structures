class Node:
    def __init__(self, prev, data, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

    def traverseBack(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.prev
        print("None")

    def insertBegin(self, ele):
        newnode = Node(None, ele, self.head)
        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode

    def insertEnd(self,ele):
        newnode=Node(None,ele,None)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
        

# Pre-inserting nodes manually
n1 = Node(None, 10, None)
n2 = Node(n1, 20, None)
n3 = Node(n2, 30, None)
n4 = Node(n3, 40, None)

n1.next = n2
n2.next = n3
n3.next = n4

dll = DoubleLinkedList()
dll.head = n1

print("Original Forward Traversal:")
dll.traverse()
print("Original Backward Traversal:")
dll.traverseBack()

ele = int(input("Enter element to insert at the beginning: "))
dll.insertBegin(ele)

ele = int(input("Enter element to insert at the end: "))
dll.insertEnd(ele)
dll.traverse()