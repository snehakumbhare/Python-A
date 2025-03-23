#Python: Return the symmetric difference between two iterables, without filtering out duplicate values
#Write a Python program to get the symmetric difference between two iterables, without filtering out duplicate values.

#Create a set from each list.
#Use a list comprehension on each of them to only keep values not contained in the previously created set of the other.
# Define a function 'symmetric_difference' that takes two lists, 'x' and 'y', as input.
def symmetric_difference(x, y):
    # Create sets '_x' and '_y' from the input lists 'x' and 'y'.
    _x, _y = set(x), set(y)
    
    # Calculate the symmetric difference of the two sets and store it in a list.
    # The symmetric difference contains elements that are unique to each set.
    symmetric_diff = [item for item in x if item not in _y] + [item for item in y if item not in _x]
    
    # Return the result.
    return symmetric_diff

# Call the 'symmetric_difference' function with two lists and print the symmetric difference.
print(symmetric_difference([10, 20, 30], [10, 20, 40])) 
