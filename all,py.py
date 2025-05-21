class Node:
    def __init__(self,element):
        self.data=element
        self.next=None
class SingleLinkedList:
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
    def deleteBegin(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            current=self.head
            self.head=current.next
            print(current.data,"deleted")
            del current

    def deleteLast(self):
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
            prev.next=None
            
    def insertbeforeanode(self,ele,key):
        if self.head is None:
            print("linkedlist is emoty , Insertion not possible")
        else:
            newnode=Node(ele)
            current=self.head
            if current.data==key:
                newnode.next=self.head
                self.head=newnode
            else:
                current=self.head
                while current.next and current.data!=key:
                    current=current.next
                if current.next:
                    newnode.next=current.next
                    current.next=newnode
                else:
                    print("node with data",key,"not found")

    def insertafteranode(self,ele,key):
        if self.head is None:
            print("linkedlist is emoty , Insertion not possible")
        else:
            newnode=Node(ele)
            current=self.head
            while current:
                if current.data==key:
                    newnode.next=current.next
                    current.next=newnode
                    break
                current=current.next
            else:
                print("node with data",key,"not found")
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

    def deletebefornode(self,key):
        if self.head is None:
            print("linkedlist is emoty , Insertion not possible")
        else:
            if self.head.next is None:
                print("List has only on element deletion not possible")
            elif self.head.data==key:
                self.head=self.head.next
            else:
                prev=self.head
                current=self.head.next
                while current.next and current.next.data!=key:
                    prev=current
                    current=current.next
                if current.next:
                    print(current.data,"deleted")
                    prev.next=current.next
                else:
                    print("Key element not found on the list ")


    def deleteafteranode(self,key):
        if self.head is None:
            print("linkedlist is emoty , Insertion not possible")
        else:
            if self.head.next is None:
                print("List has only on element deletion not possible")
            else:
                current=self.head
                while current and current.next==key:
                    current=current.next
                if current and current.next:
                    current.next=current.next.next
                else:
                    print("Key element not found on the list ")
    def ReverseList(self):
        if self.head is None:
            print("List is empty")
        else:
            current=self.head
            prev=None
            while current:
                nextnode=current.next
                current.next=prev
                prev=current
                current=nextnode
            self.head=prev
            print("List reversed successfully")
        

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
    print("\n1.Insert@Begin 2.Insert@Last1 3.Delete@Begin 4.Delete@Last 5.insert before a node  6.insert afetr the node 7. inseert at specifeis position 8. delete befor a node 9.delete after node 10.Reverse a list  11.Display 12.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        ele=int(input("Enter the element to be insertedBegin1:"))
        sll.insertBegin(ele)
    elif ch==2:
        ele=int(input("Enter the element to be insertedLast:"))
        sll.insertLast(ele)
    elif ch==3:
        sll.deleteBegin()
    elif ch==4:
        sll.deleteLast()
    elif ch==5:
        ele=int(input("Enter the element to be inserted before the node:"))
        key=int(input("Enter the element before which you want to insert:"))
        sll.insertbeforeanode(ele,key)  
    elif ch==6:
        ele=int(input("Enter the element to be inserted after the node:"))
        key=int(input("Enter the element after which you want to insert:"))
        sll.insertafteranode(ele,key)
    elif ch==7:
        ele=int(input("Enter the element to be inserted at specified position:"))
        pos=int(input("Enter the position at which you want to insert:"))
        sll.insertatspecifiedposistion(ele,pos)
    elif ch==8:
        key=int(input("Enter the element before which you want to delete:"))
        sll.deletebefornode(key)
    elif ch==9:
        key=int(input("Enter the element after which you want to delete:"))
        sll.deleteafteranode(key)
    elif ch==10:
        sll.ReverseList()
    elif ch==11:
        sll.display()
    elif ch==12:
        break

