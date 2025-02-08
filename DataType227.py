#Python: Return every element that exists in any of the two given lists once, after applying function to each element of both

#Write a  Python program to get every element that exists in any of the two given lists once, after applying the provided function to each element of both.

#Create a set by applying fn to each element in x.

#Use a list comprehension in combination with fn on y to only keep values not contained in the previously created set, _x.

#Finally, create a set from the previous result and x and transform it into a list.
# Define a function 'union_by_el' that takes two lists 'x' and 'y' and a function 'fn' as input.
def union_by_el(x, y, fn):
    # Create a set '_x' containing the results of applying the 'fn' function to each element in 'x'.
    _x = set(map(fn, x))
    # Create a list containing elements that are in 'x' and also in 'y' but only if the result of applying 'fn' to them is not in '_x'.
    result = x + [item for item in y if fn(item) not in _x]
    # Convert the result list to a set to eliminate duplicates and then back to a list.
    return list(set(result))

# Import the 'floor' function from the 'math' module.
from math import floor

# Display the result of applying 'union_by_el' to two example lists using the 'floor' function.
print(union_by_el([4.1], [2.2, 4.3], floor)) 
