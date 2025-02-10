#Python: Find the index of the first element in the given list that satisfies the provided testing function
#Write a  Python program to find the index of the first element in the given list that satisfies the provided  testing function.

#Use a list comprehension, enumerate() and next() to return the index of the first element in nums for which fn returns True.
# Define a function 'find_index' that takes a list 'nums' and a function 'fn' as input.
def find_index(nums, fn):
    # Use a generator expression to find the first index 'i' where 'fn(x)' is True for an element 'x' in 'nums'.
    return next(i for i, x in enumerate(nums) if fn(x))

# Call the 'find_index' function with an example list and a lambda function that checks if a number is odd.
print(find_index([1, 2, 3, 4], lambda n: n % 2 == 1))

