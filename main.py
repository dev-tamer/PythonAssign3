#  ---------------- PROBLEM 2 ----------------------------------------------

import random


def doMatrix(n):
    sum = 0
    num = n * n
    rows, cols = (n, n)
    a = []
    b = [[0] * cols] * rows
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(random.randint(0, 255))
        a.append(col)
    # print(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            sum = sum + a[i][j]
    mean = sum / num
    print(mean)
    b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    print(b)
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = b[i][j] - mean
    return b

print doMatrix(5)
# The time complexity of the function is O(n^2).


#  ---------------------- PROBLEM 4 & 5 -------------------------------------------------

# node class
class _Node:
    # constructor
    def __init__(self, element):
        self._element = element
        self._next = None


# linked list class
class LinkedList:
    # constructor
    def __init__(self):
        self._head = None
        self._size = 0

    # function to insert the element in to the linked list
    def insert(self, element):
        if self._head is None:
            self._head = _Node(element)
            self._size += 1
        else:
            temporary = _Node(element)
            current = self._head
            while (current._next is not None):
                current = current._next
            current._next = temporary
            self._size += 1

    # function to calculate the length of the linked list
    def length(self):
        return self._size

    # function to find the largest number in the linked list
    def max(self):
        m = 0
        current = self._head
        while (current is not None):
            if (current._element > m):
                m = current._element
            current = current._next
        return m


# function to merge two linkedlists
def merge(LinkL1, LinkL2):
    bothll = LinkedList()
    current1 = LinkL1._head
    current2 = LinkL2._head
    # iterate over both the linked lists
    while (current1 is not None and current2 is not None):
        if (current1._element <= current2._element):
            bothll.insert(current1._element)
            current1 = current1._next
        else:
            bothll.insert(current2._element)
            current2 = current2._next
    while (current1 is not None):
        bothll.insert(current1._element)
        current1 = current1._next
    while (current2 is not None):
        bothll.insert(current2._element)
        current2 = current2._next
    return bothll


# first linked list
LinkL1 = LinkedList()
LinkL1.insert(1)
LinkL1.insert(3)
LinkL1.insert(5)

# second linked list
LinkL2 = LinkedList()
LinkL2.insert(2)
LinkL2.insert(4)
LinkL2.insert(6)

# call the merged function
bothll = merge(LinkL1, LinkL2)
current = bothll._head
resutlst = []
while (current is not None):
    resutlst.append(current._element)
    current = current._next

print "The merged list is: ", resutlst
