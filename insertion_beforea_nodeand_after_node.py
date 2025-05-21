
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
    print("\n1.Insert@Begin 2.Insert@Last1 3.Delete@Begin 4.Delete@Last 5.insert before a node  6.insert afetr the node 7.Display 8.Exit")
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
        sll.display()
    elif ch==8:
        break
