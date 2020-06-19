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
    
    
    # printInfo traverses the list from the first node and prints the data of each node.
    def printInfo(self):
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
def find_intersection(list1, list2):
    if (list1.head is None or list2.head is None):
        return Solution()

    intersection = Solution()    # create a new linked list class called intersection

    # get the length of both lists
    len_list1 = list1.getCount()
    len_list2 = list2.getCount()
    count = 0
    current1 = list1.head
    current2 = list2.head

    # calculate the difference with both lists
    # if length of list is is greater than that of list2, move list 1 until it's length
    # becomes equal to that of list 2
    if (len_list1 >= len_list2):
        diff = len_list1 - len_list2  # difference between list 1 and list2
        while (count < diff):           # while list one remains longer than list 2, move list 1
            current1 = current1.next
            count = count + 1

        # while lists 1 and 2 are not NULL....check if both lists at position[i] are the same
        while (current1 is not None and current2 is not None):    
            data = current1.data     # variable "data" will receive the data in head

            # if data in list 1 is same as in list2, create a new node and insert this data
            if data == current2.data:
                node = Node(data)
                intersection.insert_at_end(node)   # call function to insert node at the end
                                              
                break            # once we find the first data in common, no need to continue
            else:
                current2 = current2.next   # move both lists to the next position
                current1 = current1.next
        return intersection                # return intersection of both lists

    # if list 2 is longer than list 1, do similar to the previous section
    else:
        diff = len_list2 - len_list1
        while (count < diff):
            current2 = current2.next
            count = count + 1

        while (current2 is not None and current1 is not None):  # while current1 is not NULL...
            data = current2.data     # variable "data" will receive the data in head

            if data == current1.data:
                node = Node(data)
                intersection.insert_at_end(node)
                                              
                break
            else:
                current1 = current1.next
                current2 = current2.next
        return intersection
 
 
list1 = Solution()
list2 = Solution()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(data)
    list1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(data)
    list2.insert_at_end(node)
 

intersection = find_intersection(list1, list2)
 

print('Their intersection is: ')
intersection.printInfo()
print()


"""
Given that there are two linked lists to be compared, each with perhaps different
sizes, the time complexity for this algorithm is O(n), where n = m * p,
 where m is the length of  list 1 and p is the length of list 2. 

"""