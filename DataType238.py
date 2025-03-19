#Python: Find the value of the first element in the given list that satisfies the provided testing function

#Write a Python program to find the value of the first element in the given list that satisfies the provided testing function.

#Use a list comprehension and next() to return the first element in lst for which fn returns True.

# Define a function 'find' that takes a list 'lst' and a function 'fn' as input.
def find(lst, fn):
    # Use a generator expression to find the first element 'x' in the list 'lst' for which 'fn(x)' is true.
    # The 'next' function is used to retrieve the first matching element.
    return next(x for x in lst if fn(x))

# Call the 'find' function with a list and a lambda function to find the first odd number in the list.
# Print the result.
print(find([1, 2, 3, 4], lambda n: n % 2 == 1))
# Call the 'find' function again with a lambda function to find the first even number in the list.
# Print the result.
print(find([1, 2, 3, 4], lambda n: n % 2 == 0))
