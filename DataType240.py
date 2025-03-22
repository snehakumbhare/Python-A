#Python: Create a dictionary with the unique values of a list as keys and their frequencies as the values

#Write a Python program to create a dictionary with the unique values of a given list as keys and their frequencies as values.

#Use collections.defaultdict() to store the frequencies of each unique element.
#Use dict() to return a dictionary with the unique elements of the list as keys and their frequencies as the values.
# Import the 'defaultdict' class from the 'collections' module to create a dictionary with default values.
from collections import defaultdict

# Define a function 'frequencies' that takes a list 'lst' as input.
def frequencies(lst):
    # Create an empty dictionary with default integer values.
    freq = defaultdict(int)
    
    # Iterate over the elements 'val' in the input list 'lst'.
    for val in lst:
        # Increase the count of the element 'val' in the dictionary by 1.
        freq[val] += 1
    
    # Convert the defaultdict to a regular dictionary and return the result.
    return dict(freq)

# Call the 'frequencies' function with a list of strings to count the frequency of each string.
# Print the result.
print(frequencies(['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f']))

# Call the 'frequencies' function again with a list of integers to count the frequency of each integer.
# Print the result.
print(frequencies([3, 4, 7, 5, 9, 3, 4, 5, 0, 3, 2, 3]))
