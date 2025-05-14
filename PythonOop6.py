#Python Object-Oriented Programming: Linked list class with insertion, deletion, and display methods

#Write a Python program to create a class representing a linked list data structure. 
#Include methods for displaying linked list data, inserting and deleting nodes.

# Define a class called Node to represent a node in a linked list
class Node:
    # Initialize the Node object with data and set the next pointer to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class called LinkedList to represent a singly linked list
class LinkedList:
    # Initialize the linked list with an empty head node
    def __init__(self):
        self.head = None

    # Display the elements in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Insert a new node with the given data at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node with the given data from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

# Example usage
# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Display the initial linked list
print("Initial Linked List:")
linked_list.display()

# Insert a new node with data 5 into the linked list
linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()

# Delete a node with data 2 from the linked list
linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display() 
