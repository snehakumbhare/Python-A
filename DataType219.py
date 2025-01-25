#Python: Map the values of a list to a dictionary using a function

#Write a  Python program to map the values of a list to a dictionary using a function, 
#where the key-value pairs consist of the original value as the key and the result of the function as the value.

#Use map() to apply fn to each value of the list.
#Use zip() to pair original values to the values produced by fn.
#Use dict() to return an appropriate dictionary.

# Define a function called 'map_dictionary' that takes an iterable 'itr' and a function 'fn' as arguments.
def map_dictionary(itr, fn):
  # Create a dictionary by zipping the iterable 'itr' and the result of applying the function 'fn' to each element in 'itr'.
  return dict(zip(itr, map(fn, itr)))

# Example usage: Use the 'map_dictionary' function to create a dictionary where the keys are elements from the list [1, 2, 3] and the values are the squares of those elements.
print(map_dictionary([1, 2, 3], lambda x: x * x))
