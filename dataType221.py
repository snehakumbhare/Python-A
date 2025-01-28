#Python: Get the difference between two given lists, after applying the provided function to each list element of both
#Write a  Python program to get the difference between two given lists, after applying the provided function to each list element of both.

#Create a set, using map() to apply fn to each element in b.
#Use a list comprehension in combination with fn on a to only keep values not contained in the previously created set, _b.
# Import the 'floor' function from the 'math' module.
from math import floor
# Define a function called 'difference_by' that takes three arguments: 'a', 'b', and 'fn'.
def difference_by(a, b, fn):
  # Create a set '_b' by applying the 'fn' function to each element in 'b'.
  _b = set(map(fn, b))
  # Return a list of items in 'a' for which the result of applying 'fn' is not in '_b'.
  return [item for item in a if fn(item) not in _b]

# Example 1: Find the difference between two lists after applying the 'floor' function.
print(difference_by([2.1, 1.2], [2.3, 3.4], floor))

# Example 2: Find the difference between two lists of dictionaries using a custom lambda function.
print(difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']))
