#Python: Get a list with n elements removed from the left, right
#Write a Python program to get a list with n elements removed from the left and right.
# Define a function named 'drop_left_right' that removes elements from the left and right of a list.
# It takes a list 'a' and an optional parameter 'n' specifying the number of elements to remove from both sides.
def drop_left_right(a, n=1):
    # Return a tuple of two lists: elements from index 'n' to the end and elements from the beginning to 'n' from the original list 'a'.
    return a[n:], a[:-n]

# Create a sample list 'nums' with integer elements.
nums = [1, 2, 3]
# Print the original list elements.
print("Original list elements:")
print(nums)
# Use the 'drop_left_right' function to remove 1 element from the left of the list and store the results in 'result'.
result = drop_left_right(nums)
# Print the list with 1 element removed from the left.
print("Remove 1 element from the left of the said list:")
print(result[0])
# Print the list with 1 element removed from the right.
print("Remove 1 element from the right of the said list:")
print(result[1])

# Create another sample list 'nums' with integer elements.
nums = [1, 2, 3, 4]
# Print the original list elements.
print("\nOriginal list elements:")
print(nums)
# Use the 'drop_left_right' function to remove 2 elements from the left of the list and store the results in 'result'.
result = drop_left_right(nums, 2)
# Print the list with 2 elements removed from the left.
print("Remove 2 elements from the left of the said list:")
print(result[0])
# Print the list with 2 elements removed from the right.
print("Remove 2 elements from the right of the said list:")
print(result[1])

# Create another sample list 'nums' with integer elements.
nums = [1, 2, 3, 4, 5, 6]
# Print the original list elements.
print("\nOriginal list elements:")
print(nums)
# Use the 'drop_left_right' function without specifying 'n' to remove 1 element from both left and right.
result = drop_left_right(nums)
# Print the list with 1 element removed from both left and right.
print("Remove 1 element from both left and right of the said list:")
print(result[0])
print("Remove 1 element from both left and right of the said list:")
print(result[1])

