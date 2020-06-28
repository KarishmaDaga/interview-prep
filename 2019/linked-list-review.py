"""
Linked List
- elements are linked using pointers

Advantages:
- dynamic size
- ease of insert/delete operations

Disadvantages:
- must access elements sequentially
"""

# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None

# Given a singly linked list and a position, delete a linked list node at the given position.
    def deleteNode(self, position): 
  
        # If linked list is empty 
        if self.head == None: 
            return 
  
        # Store head node 
        temp = self.head 
  
        # If head needs to be removed 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
        temp.next = next 
         
         
    # This function counts number of nodes in Linked List 
       # iteratively, given 'node' as starting node. 
       def getCount(self): 
           temp = self.head # Initialise temp 
           count = 0 # Initialise count
           
         while (temp):
            count += 1
            temp = temp.next
         return count
      
  # Returns data at given index in linked list 
    def getNth(self, index): 
        current = self.head # Initialise temp 
        count = 0 # Index of current node
      
      while (current):
         if count == index:
            return current.data
         else:
            count += 1
            current.next
            
