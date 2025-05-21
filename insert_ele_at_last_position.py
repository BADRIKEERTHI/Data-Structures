class Node:
    def __init__(self,element):
        self.data=element
        self.next=None

class SingleLinkedList():
    def __init__(self):
        self.head=None

    def insertLast(self,ele):
        newnode=Node(ele) #creating a new node
        if self.head is None: #if head is none linkedlist is empty
            self.head=newnode #set head to point to the newnode
        else:
            current=self.head #set current=head
            while current.next!=None: #repeat above steps while current!=None
                current=current.next #update current to its next {{{End of loop}}}
            current.next=newnode  #set current.next to newnode  {{exit }}}

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
    
    def insertatspecifiedposistion(self,ele,pos):
        if pos<1:
            print("Invalid position")
            return              
        newnode=Node(ele)
        if pos==0:
            newnode.next=self.head
            self.head=newnode
            return
        current=self.head
        index=0
        while current and index<pos-1:
            current=current.next
            index+=1
        if current is None:
            print("Position out of range")
        else:
            newnode.next=current.next
            current.next=newnode
            
sll=SingleLinkedList()
while True:
    print("\n1.Insert@last 2.Display 3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        ele=int(input("Enter the element to be inserted:"))
        sll.insertLast(ele)
    elif ch==2:
        sll.display()
    elif ch==3:
        break
#sll.insert(55)
#sll.display()
#sll.insert(66)
#sll.display()
#sll.insert(77)
#sll.display()

