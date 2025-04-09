#Python: Perform a deep flattens a list
#Write a Python program to perform a deep flattening of a list.

#Use recursion.
#Use isinstance() with collections.abc.Iterable to check if an element is iterable.
#If it is iterable, apply deep_flatten() recursively, otherwise return [lst].
from collections.abc import Iterable

# Define a function to deeply flatten a nested list.
def deep_flatten(lst):
    # Check if the input is an iterable (e.g., a list or nested list).
    if isinstance(lst, Iterable):
        # Use list comprehensions to recursively flatten nested lists.
        return [a for i in lst for a in deep_flatten(i)]
    else:
        # If the input is not an iterable, return a list containing the input element.
        return [lst]

# Example 1
nums = [1, [2], [[3], [4], 5], 6]
print("Original list elements:")
print(nums) 
print()
print("Deep flatten the said list:")
print(deep_flatten(nums))

# Example 2
nums = [[[1, 2, 3], [4, 5]], 6]
print("\nOriginal list elements:")
print(nums) 
print()
print("Deep flatten the said list:")
print(deep_flatten(nums)) 
