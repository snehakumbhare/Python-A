#Develop a Custom Iterator for Tree data structures in Python

#Write a Python program to develop a custom iterator that iterates over a tree data structure.

# Define a class representing a node in a tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # Initialize an empty list to store child nodes

    def add_child(self, child_node):
        self.children.append(child_node)  # Add a child node to the list of children

# Define a class implementing a custom iterator for tree traversal
class TreeIterator:
    def __init__(self, root):
        self.stack = [root]  # Initialize stack with root node

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:  # If stack is empty, no more nodes to traverse
            raise StopIteration
        node = self.stack.pop()  # Get the top node from stack
        for child in reversed(node.children):  # Add children to stack in reverse order
            self.stack.append(child)
        return node.value

# Example usage:
if __name__ == "__main__":
    # Create a tree with a root node and some child nodes
    root = TreeNode(1)
    root.add_child(TreeNode(2))
    root.add_child(TreeNode(3))
    root.children[0].add_child(TreeNode(4))
    root.children[0].add_child(TreeNode(5))
    root.children[1].add_child(TreeNode(6))

    # Create a TreeIterator instance and iterate over the tree
    tree_iterator = TreeIterator(root)
    for value in tree_iterator:
        print(value)


