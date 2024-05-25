class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SinglyLinkedList:
    def __init__(self):
        self.__size=0
        self.head=None
        self.tail=None

    def is_empty(self):
        return self.__size==0                   
    
    def size(self):
        return self.__size

    def append(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:                                       # agar empty nhi h toh 
            trav=self.head
            while trav.next:                        # end pe pahunch gye
                trav=trav.next
            trav.next=newNode                       # append kr die

        self.__size +=1                             

    def add_First(self,data):
        newnode=Node(data)
        if self.size()==0:                        # ek bhi nhi h toh whi add krdo
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head               # else head ko update krdo
            self.head.next=self.head.next.next
            self.head=newnode
            
        self.__size+=1

    def add_Last(self,data):
        newNode=Node(data)
        if(self.size()==0):
            self.head=newNode
            self.tail=newNode
        else:                                # last me add krne ke liye
            trav=self.head
            while(trav.next):
                trav=trav.next
            trav.next=newNode
            newNode.next=None
        
        self.__size+=1

    def add_index(self,index,data):
        if(index < 0 or index > self.size()):               # index out of bound check kia 
            raise Exception ("Invalid Index")
        if index==0:                            
            self.add_First(data)                            # aage add krna h toh
        elif index==self.size():
            self.append(data)                               # agar same h toh
        else:
            trav=self.head              
            for _ in range(index - 1):                      # index tk pahunch gaye
                trav = trav.next
            newnode = Node(data, trav.next)
            trav.next = newnode                             # update krdo
            self.__size += 1

    def remove_First(self):                 
        if self.is_empty():
            raise Exception ("Can't remove : List is empty")
        self.head=self.head.next                           # pehla removed
        
        self.__size-=1

    def remove_last(self):
        if self.is_empty():
            raise Exception ("Can't remove : List is empty")
        if self.size()==1:
            self.head=None              # head waala none hogya (mtlb remove hogya)
        else:
            prev = None
            trav = self.head
            while trav.next:
                prev = trav
                trav = trav.next
            prev.next = None
        self.__size -= 1

    def remove_at(self,index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range")            # index out of bond check kia
        if index == 0:
            self.remove_first()                               # 0 h toh aage ka hi hata dia
        else:
            trav = self.head                                
            for _ in range(index - 1):
                trav = trav.next
            trav.next = trav.next.next
            self.__size -= 1

    def reverse(self):
        prev = None
        trav = self.head
        while trav:
            next_node = trav.next
            trav.next = prev
            prev = trav
            trav = next_node
        self.head = prev

    # Merging lists

    def merge_list(self,newl):
        if self.is_empty():
            self.head=newl.head
        else:
            trav=self.head                                     # trav = head
            while trav.next:
                trav=trav.next                                 # end pe aa gye puraane waale list ke
            trav.next=newl.head
        self.__size += newl.__size

    # Middle of list

    def middle_list(self):
        if self.is_empty():
            raise Exception ("List is empty..")
        s=self.head                               # slow pointer
        f=self.head                               # fast pointer
        while f and f.next:
            s=s.next                              # speed = 1
            f=f.next.next                         # speed = 2

        return s.data
        
    def print_list(self):
        trav = self.head
        while trav:
            print(trav.data, end=' ')
            trav = trav.next
        print()

ll=SinglyLinkedList()

# Question 1:

ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)
ll.print_list()
print(ll.size())
print()
# Question 2:

ll.remove_at(2)
ll.print_list()
print(ll.size())
print()

# Question 3:

print("Size of linked list :",ll.size())
print()

# Question 4:

print(ll.is_empty())
print()

# Question 5:



# Question 6:

ll.reverse()
ll.print_list()
print()

# Question 7:

ll.add_Last(15)
ll.add_Last(25)
ll.print_list()
print()

# Question 8:

ll.add_First(30)
ll.add_First(35)
ll.print_list()
print()


# Question 9:

# To merge we have to first make linked list . So, let's make:
l2=SinglyLinkedList()
l2.append(40)
l2.append(45)
l2.append(50)
ll.merge_list(l2)
print("Merging list :")
ll.print_list()
print("Length of merged list :",ll.size())
print()

# Question 10:

# Question 11:

print("Middle one :",ll.middle_list())
print()
