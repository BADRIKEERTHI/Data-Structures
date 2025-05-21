class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def insertLast(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            newnode.next=newnode
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=newnode
            newnode.next=self.head
            cll.display()

    def insertBegin(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
            newnode.next=newnode
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=newnode
            newnode.next=self.head
            self.head=newnode
            cll.display()

    def deleteBegin(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next ==self.head:
            print(self.head.data,"deleted, list i snow empty")
            self.head=None
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            temp=self.head
            self.head=self.head.next
            current.next=self.head
            print(temp.data,"deleted")
            del temp
            cll.display()

    def deleteLast(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next==self.head:
            print(self.head.data,"deleted, list is now empty")
            self.head=None
        else:
            current=self.head
            while current.next.next!=self.head:
                current=current.next
            temp=current.next
            current.next=self.head
            print(temp.data,"deleted")
            del temp
            cll.display()

    def display(self):
        if not self.head:
            print("List is empty")
            return 
        current=self.head
        while True:
            print(current.data,end='->')
            current=current.next
            if current==self.head:
                break
        print(None)

cll=CircularLinkedList()
cll.insertLast(12)
cll.insertLast(23)
cll.insertLast(34)
cll.insertLast(45)

print("1.Display \n2.Insert at last \n3.Insert at begin \n4.Delete at begin")   
while True:
    ch=int(input("Enter operation to be performed: "))
    if ch==1:
        print("Circular linked list : ")
        cll.display()
    elif ch==2:
        val=int(input("Enter a value to insert at last: "))
        cll.insertLast(val)
    elif ch==3:
        val=int(input("Enter a value to insert at last: "))
        cll.insertBegin(val)
    elif ch==4:
        print("Deleting 1st element")
        cll.deleteBegin()
    elif ch==5:
        print("Deleting last element")
        cll.deleteLast()
        