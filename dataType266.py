#Python: Cumulative sum of the elements of a given list

#Write a Python program to get the cumulative sum of the elements of a given list.
# Import the 'accumulate' function from the 'itertools' module.
from itertools import accumulate

# Define a function named 'cumsum' that computes the cumulative sum of a list.
def cumsum(lst):
    # Use the 'accumulate' function to calculate the cumulative sum and convert it to a list.
    return list(accumulate(lst))

# Create a sample list 'nums' with integer elements.
nums = [1, 2, 3, 4]
# Print the original list elements.
print("Original list elements:")
print(nums)
# Calculate and print the cumulative sum of the elements in the list using the 'cumsum' function.
print("Cumulative sum of the elements of the said list:")
print(cumsum(nums))

# Create another sample list 'nums' with integer elements, including negative values.
nums = [-1, -2, -3, 4]
# Print the original list elements.
print("\nOriginal list elements:")
print(nums)
# Calculate and print the cumulative sum of the elements in the list using the 'cumsum' function.
print("Cumulative sum of the elements of the said list:")
print(cumsum(nums)) 

