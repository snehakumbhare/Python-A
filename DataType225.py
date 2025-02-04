#Python: Get a list of elements that exist in both lists
#Write a  Python program to get a list of elements that exist in both lists, after applying the provided function to each list element of both.

#Create a set, using map() to apply fn to each element in b.
#Use a list comprehension in combination with fn on a to only keep values contained in both lists.
# Import the necessary modules and functions.
from math import floor

# Define a function 'intersection_by' that takes two lists 'a' and 'b' and a function 'fn' as input.
def intersection_by(a, b, fn):
    # Create a set '_b' containing the results of applying 'fn' to each element in list 'b'.
    _b = set(map(fn, b))
    # Return a list containing elements from list 'a' where 'fn(item)' is in the set '_b'.
    return [item for item in a if fn(item) in _b]
	
# Provide an example of using 'intersection_by' function to find the intersection of two lists using 'floor' function as the key.
print(intersection_by([2.1, 1.2], [2.3, 3.4], floor))
