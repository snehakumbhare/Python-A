#Python: Find the value of the last element in the given list that satisfies the provided testing function

#Write a  Python program to find the value of the last element in the given list that satisfies the provided testing function.

#Use a list comprehension and next() to return the last element in lst for which fn returns True.

# Define a function 'find_last' that takes a list 'lst' and a function 'fn' as input.
def find_last(lst, fn):
    # Use a generator expression to find the last element 'x' in the reversed list 'lst[::-1]'
    # for which 'fn(x)' is true. The 'next' function is used to retrieve the last matching element.
    return next(x for x in lst[::-1] if fn(x))

# Call the 'find_last' function with a list and a lambda function to find the last odd number in the list.
# Print the result.
print(find_last([1, 2, 3, 4], lambda n: n % 2 == 1))
# Call the 'find_last' function again with a lambda function to find the last even number in the list.
# Print the result.
print(find_last([1, 2, 3, 4], lambda n: n % 2 == 0))
