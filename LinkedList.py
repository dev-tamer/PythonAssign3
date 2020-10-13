#node class
class _Node:
   #constructor
   def __init__(self, element):
       #initialize the element
       self._element = element
       self._next = None
#linked list class
class LinkedList:
   #constructor
   def __init__(self):
       #initialize the head to None
       self._head = None
       self._size = 0
   #function to insert the element in to the linked list
   def insert(self, element):
       #if the head is none, insert at the head
       if self._head is None:
           self._head = _Node(element)
           self._size += 1
       else:
           #create a node object
           temporary = _Node(element)
           #initialize the current to the head
           current = self._head
           #iterate over the linked list
           while(current._next is not None):
               #move to the next node
               current = current._next
           #store the given node at the last
           current._next = temporary
           self._size += 1
   #function to calculate the length of the linked list
   def length(self):
       #return the size variable
       return self._size
   #function to calculate the maximum element in the linked list
   def max(self):
       #initialize the max to 0
       m = 0
       #initialize the variable to head
       current = self._head
       #iterate over the linked list
       while(current is not None):
           #if the current element greater than max
           if(current._element > m):
               #update max
               m = current._element
           #move to the next node
           current = current._next
       return m
#function to merge two linkedlists
def merge(LinkL1, LinkL2):
   #create a new empty linked list
   bothll = LinkedList()
   #initialize current1 to head of first linked list
   current1 = LinkL1._head
   #initialize current2 to head of second linked list
   current2 = LinkL2._head
   #iterate over both the linked lists
   while(current1 is not None and current2 is not None):
       #if the current element of first linked list less than current element of second linked list
       if(current1._element <= current2._element):
           #insert to new linked list
           bothll.insert(current1._element)
           #move to the next element in first linked list
           current1 = current1._next
       #if the current element of second linked list less than current element of first linked list
       else:
           #insert to new linked list
           bothll.insert(current2._element)
           #move to the next node in second linked list
           current2 = current2._next
   #iterate over the remaining elements in first linked list, if any
   while(current1 is not None):
       #insert into the new list
       bothll.insert(current1._element)
       #Move to next node
       current1 = current1._next
   #iterate over the remaining elements in the second linked list, if any
   while(current2 is not None):
       #insert into te new list
       bothll.insert(current2._element)
       #move to the next node
       current2 = current2._next
   return bothll
#create first linked list
LinkL1 = LinkedList()
LinkL1.insert(1)
LinkL1.insert(3)
LinkL1.insert(5)

#create second linked list
LinkL2 = LinkedList()
LinkL2.insert(2)
LinkL2.insert(4)
LinkL2.insert(6)
#call the function
bothll = merge(LinkL1, LinkL2)
#print the elements in the new linked list
print("The elements in the merged linked list are")
current = bothll._head
while(current is not None):
   print(current._element)
   current = current._next