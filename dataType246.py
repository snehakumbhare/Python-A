#Python: Calculate the difference between two iterables, without filtering duplicate values

#Write a Python program to calculate the difference between two iterables, without filtering duplicate values.

#Create a set from y.

#Use a list comprehension on x to only keep values not contained in the previously created set, _y.

# Define a function 'difference' that takes two lists 'x' and 'y'.

# It converts 'y' into a set for faster membership checking.
# It returns a new list containing elements that are in 'x' but not in 'y'.
def difference(x, y):
    _y = set(y)
    return [item for item in x if item not in _y]

# Call the 'difference' function with two lists and print the result.
print(difference([1, 2, 3], [1, 2, 4]))
