class Node():
    def __init__(self,element):
        self.data=element
        self.next=None
class SingleLinkedList():
    def __init__(self):
        self.head=None
        
    def insertBegin(self,ele):
        newnode=Node(ele)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def insertLast(self,ele):
            newnode=Node(ele) #creating a new node
            if self.head is None: #if head is none linkedlist is empty
                self.head=newnode #set head to point to the newnode
            else:
                current=self.head #set current=head
                while current.next!=None: #repeat above steps while current!=None
                    current=current.next #update current to its next {{{End of loop}}}
                current.next=newnode  #set current.next to newnode  {{exit }}}

    def deleteLast(self):
        if self.head is None:
            print("Linkedlist is empty")
        elif self.head.next is None:
            del self.head
            self
        else:
            second_last=self.head
            while second_last.next.next:
                second_last=second_last.next
            del second_last.next
            second_last.next=None     



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
    print("\n1.insert@Begin 2.insert@Last 3.Delete@Last1 4.Display 5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        ele=int(input("Enter the element to be inserted at Begining:"))
        sll.insertBegin(ele)
    elif ch==2:
        ele=int(input("Enter the element to be inserted at Last:"))
        sll.insertLast(ele)
    elif ch==3:
        sll.deleteLast()
    elif ch==4:
        sll.display()
    elif ch==5:
        break

''' def deleteLast(self):
        if self.head is None:
            print("Linkedlist is empty")
        elif self.head.next==None:
           print(self.head.data,"deleted")
           self.head=None
           else:
            prev=self.head
            current=self.head.next
            while current.next!=None:
                prev=current
                current=current.next
            print(current.data,"deleted")
            prev.next=None   '''
            