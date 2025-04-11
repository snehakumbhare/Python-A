#Python: Find the powerset of a given iterable
#Write a Python program to get the powerset of a given iterable.
from itertools import chain, combinations

# Define a function to generate the powerset of an iterable.
def powerset(iterable):
    s = list(iterable)  # Convert the input iterable to a list.
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

# Example 1
nums = [1, 2]
print("Original list elements:")
print(nums)
print("Powerset of the said list:")
print(powerset(nums))

# Example 2
nums = [1, 2, 3, 4]
print("\nOriginal list elements:")
print(nums)
print("Powerset of the said list:")
print(powerset(nums)) 
