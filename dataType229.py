#Python: Find the indexes of all elements in the given list that satisfy the provided testing function
#Write a Python program to find the indexes of all elements in the given list that satisfy the provided testing function.

# Use enumerate() and a list comprehension to return the indexes of the all element in lst for which fn returns True.
# Define a function 'find_index_of_all' that takes a list 'lst' and a function 'fn' as input.
def find_index_of_all(lst, fn):
    # Use a list comprehension to find and collect the indices 'i' where 'fn(x)' is True for an element 'x' in 'lst'.
    return [i for i, x in enumerate(lst) if fn(x)]

# Call the 'find_index_of_all' function with an example list and a lambda function that checks if a number is odd.
print(find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1)) 
