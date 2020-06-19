# define linked list node with data (message) and next
class Node:
    def __init__(self, message):
        self.data = message
        self.next = None
 
# Create a class Solution with instance variable head. 
class Solution:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    # Create an instance of the Solution and append message entered by user to it
    def append(self, message):
        if self.last_node is None:
            self.head = Node(message)   
            self.last_node = self.head
        else:
            self.last_node.next = Node(message)
            self.last_node = self.last_node.next
    
    # The method get_prev_node takes a reference node as argument
    # and returns the previous node. It returns None when the reference node is the first node.
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    # The method remove takes a node as argument and removes it from the list.
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    # printInfo traverses the list from the first node and prints the data of each node.
    def printInfo(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 # function to remove duplicates from the list
def remove_duplicates(linkedList):
    current1 = linkedList.head
    while current1:
        data = current1.data
        current2 = current1.next
        while current2:
            if current2.data == data:
                linkedList.remove(current2)
            current2 = current2.next
        current1 = current1.next
 
 
linked_list = Solution()

count = 1
while(count==1):
    data_list = input('Please enter the messages separated by double space: ').split()
    for message in data_list:
        linked_list.append(message)
    count = input("Do you want to exit? yes/no (1/0)")
    count = int(count)

 
remove_duplicates(linked_list)
 
print('The list with duplicates removed: ')
linked_list.printInfo()