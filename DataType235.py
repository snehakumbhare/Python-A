#Python: Find the items that are parity outliers in a given list

#Write a Python program to find items that are parity outliers in a given list.

#Use collections.Counter with a list comprehension to count even and odd values in the list.

#Use collections.Counter.most_common() to get the most common parity.

#Use a list comprehension to find all elements that do not match the most common parity.

# Import the 'Counter' class from the 'collections' module.
from collections import Counter

# Define a function 'find_parity_outliers' that takes a list of numbers 'nums' as input.
def find_parity_outliers(nums):
    # Use a list comprehension to iterate through the numbers 'x' in 'nums'.
    # For each number 'x', check if it has a different parity (odd or even) compared to the most common parity in the 'nums'.
    # The 'most_common' method of 'Counter' returns a list of tuples where the first element is the most common parity (0 for even, 1 for odd) and the second element is the count.
    # Return a list of numbers where the parity is different from the most common parity in 'nums'.
    return [
        x for x in nums
        if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
    ]

# Call the 'find_parity_outliers' function with example lists of numbers and print the results.
print(find_parity_outliers([1, 2, 3, 4, 6]))
print(find_parity_outliers([1, 2, 3, 4, 5, 6, 7])) 
