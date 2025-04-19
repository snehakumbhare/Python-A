#Python: Create a two-dimensional list from given list of lists

#Write a Python program to create a two-dimensional list from a given list of lists.

#Use *nums to get the provided list as tuples.

#Use zip() in combination with list() to create the transpose of the given two-dimensional list.
# Define a function named 'two_dimensional_list' that takes a list of lists as input.
def two_dimensional_list(nums):
    # Use the 'zip' function to transpose the given two-dimensional list.
    return list(zip(*nums))
    # The '*' operator is used to unpack the sublists as separate arguments to 'zip.'

# Test the 'two_dimensional_list' function with different two-dimensional lists.
print(two_dimensional_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
# Transpose a 4x3 matrix. (Expected output: [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)])

print(two_dimensional_list([[1, 2], [4, 5]]))
# Transpose a 2x2 matrix. (Expected output: [(1, 4), (2, 5)])

