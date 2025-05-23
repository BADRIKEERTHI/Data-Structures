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

    def InsertAfter(self,ele,key):
        newnode=Node(None,ele,None)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp and  temp.data!=key:
            temp=temp.next
        if temp==None:
            print("Key not found")
            return
        newnode.prev=temp
        newnode.next=temp.next
        if temp.next!=None:
            temp.next.prev=newnode
        temp.next=newnode
    
    def InsertBefore(self,ele,key):
        newnode=Node(None,ele,None)
        if self.head==None:
            self.head=newnode
        temp=self.head
        while temp and  temp.data!=key:
            temp=temp.next
        if temp==None:
            print("Key not found")
            return
        newnode.next=temp
        newnode.prev=temp.prev
        if temp.prev!=None:
            temp.prev.next=newnode
        else:
            self.head=newnode
        temp.prev=newnode

    def DeleteBegin(self,ele):
        if self.head==None:
            print("List is empty")
        if self.head.next==None:
            self.head=None
        temp=self.head
        self.head=self.head.next
        self.head.prev=None
        del temp
    
    def DeleteEnd(self,ele):
        if self.head==None:
            print("Dll id empty")
        if self.head.next==None:
            self.head=None

        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.prev.next=None
        del temp
    
    def Delete_at_specifiednode(self,key,ele):
        if self.head==None:
            print("e\list s empty")
        temp=self.head
        while temp!=None and temp.data!=key:
            temp=temp.next
        if temp==None:
            print("node not found")
        if temp.next==None:
            print("none to be delete dnt found")
            eleminate=temp.next
            temp.next=eleminate.next
        if eleminate.next!=None:
            eleminate.next.prev=temp
        del eleminate



    




        

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

ele = int(input("Enter element to insert after a key: "))
key = int(input("Enter key to insert after: "))
dll.InsertAfter(ele, key)
dll.traverse()

ele = int(input("Enter element to insert before a key: "))
key = int(input("Enter key to insert before: "))
dll.InsertBefore(ele, key)
dll.traverse()

print("List after deleting the first element:")
dll.DeleteBegin(ele)
dll.traverse()

print("list after Delete at the End ")
dll.DeleteEnd(ele)
dll.traverse()

key=int(input("enter the element you want to eliminate "))
dll.Delete_at_specifiednode(key,ele)
dll.traverse()


