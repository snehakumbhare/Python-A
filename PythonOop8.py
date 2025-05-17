#Python Object-Oriented Programming: Stack class with push, pop, and display methods

#Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display the items in the stack
    def display(self):
        print("Stack items:", self.items)

# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Display the items in the stack
stack.display()

# Pop items from the stack and print the popped items
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)

# Display the updated items in the stack
stack.display()
