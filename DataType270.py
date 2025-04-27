#Python: Check if there are duplicate values in a given flat list

#Write a Python program to check if there are duplicate values in a given flat list.

#Use set() on the given list to remove duplicates, compare its length with the length of the list.
# Define a function named 'has_duplicates' to check if a list has duplicate values.
# It takes a single parameter, 'lst', which is the list to be checked.
def has_duplicates(lst):
    # Check if the length of the list is not equal to the length of the set of the list.
    # If the lengths are not equal, there are duplicates in the list.
    return len(lst) != len(set(lst))

# Create a list of numbers and check for duplicates.
nums = [1, 2, 3, 4, 5, 6, 7]
print("Original list:")
print(nums)
# Check if there are duplicate values in the given list using the 'has_duplicates' function.
print("Check if there are duplicate values in the said given flat list:")
print(has_duplicates(nums))

# Create another list with duplicate values and check for duplicates.
nums = [1, 2, 3, 3, 4, 5, 5, 6, 7]
print("\nOriginal list:")
print(nums)
# Check if there are duplicate values in the given list using the 'has_duplicates' function.
print("Check if there are duplicate values in the said given flat list:")
print(has_duplicates(nums))

