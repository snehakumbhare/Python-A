#Python: Symmetric difference between two lists, after applying the provided function to each list element of both

#Write a Python program to get the symmetric difference between two lists, after applying the provided function to each list element of both.

#Create a set by applying fn to each element in every list.
#Use a list comprehension in combination with fn on each of them to only keep values not contained in the previously created set of the other.
# Define a function 'symmetric_difference_by' that takes two lists 'a' and 'b' and a function 'fn' as input.
def symmetric_difference_by(a, b, fn):
    # Create sets '_a' and '_b' containing the results of applying the 'fn' function to each element in 'a' and 'b'.
    (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
    # Find the elements in 'a' that are not in '_b' and the elements in 'b' that are not in '_a'.
    # Combine these two sets and return the result as a list.
    return [item for item in a if fn(item) not in _b] + [item for item in b if fn(item) not in _a]

# Import the 'floor' function from the 'math' module.
from math import floor

# Display the result of applying 'symmetric_difference_by' to two example lists using the 'floor' function.
print(symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor)) 

