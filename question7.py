"""
Write a method that receives two singly linked lists and returns the intersecting
node of the two lists (if exists). Intersection is defined by reference, not value
"""


# Create class node with data and pointer to next node
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
 # Create Solution
class Solution:
    def __init__(self):
        self.head = None
  
    # insert_at_end inserts a node at the last position of the list
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    
    # printData traverses the list from the first node and prints the data of each node.
    def printData(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

    # This function counts number of nodes in Linked List 
    # recursively, given 'node' as starting node. 
    def getCountRec(self, node): 
        if (not node): # Base case 
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 
      
        # A wrapper over getCountRec() 
    def getCount(self): 
        return self.getCountRec(self.head)
 
 
 # ind_intersection returns the intersection of the two linked lists passed to it
def find_intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return Solution()

    intersection = Solution()    # create a new linked list class called intersection

    # get the length of both lists
    len_llist1 = llist1.getCount()
    len_llist2 = llist2.getCount()
    count = 0
    current1 = llist1.head
    current2 = llist2.head

    # calculate the difference with both lists
    if (len_llist1 >= len_llist2):
        diff = len_llist1 - len_llist2
        while (count < diff):
            current1 = current1.next
            count = count + 1

        while (current1 is not None and current2 is not None):              # while current1 is not NULL...
            data = current1.data     # variable "data" will receive the data in head

            if data == current2.data:
                node = Node(data)
                intersection.insert_at_end(node)
                                              
                break
            else:
                current2 = current2.next
                current1 = current1.next
        return intersection

    else:
        diff = len_llist2 - len_llist1
        while (count < diff):
            current2 = current2.next
            count = count + 1

        while (current2 is not None and current1 is not None):              # while current1 is not NULL...
            data = current2.data     # variable "data" will receive the data in head

            if data == current1.data:
                node = Node(data)
                intersection.insert_at_end(node)
                                              
                break
            else:
                current1 = current1.next
                current2 = current2.next
        return intersection
 
 
a_llist1 = Solution()
a_llist2 = Solution()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(data)
    a_llist1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(data)
    a_llist2.insert_at_end(node)
 

intersection = find_intersection(a_llist1, a_llist2)
 

print('Their intersection: ')
intersection.printData()
print()