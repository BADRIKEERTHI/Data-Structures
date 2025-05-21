
# create a NEW NODE with the given data
#if HEAD is None (linkedlist is empty)
#   set HEAD to point to the NEW NODE
#ELSE
#  set the NEWNODE.NEXT to point to HEAD
#  update HEAD=NEWNODE
#  Exit 
class Node():
    def __init__(self,element):
        self.data=element
        self.next=None
class SingleLinkedList():
    def __init__(self):
        self.head=None
        
    def insertBegin(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
sll=SingleLinkedList()
while True:
    print("\n1.Insert@Begin 2.Display 3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        ele=int(input("Enter the element to be inserted:"))
        sll.insertBegin(ele)
    elif ch==2:
        sll.display()
    elif ch==3:
        break