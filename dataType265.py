#Python: Casts the provided value as a list if it's not one
#Write a Python program to cast the provided value as a list if it's not one.

#Use isinstance() to check if the given value is enumerable.
#Return it by using list() or encapsulated in a list accordingly.
# Define a function named 'cast_list' that converts various data types to a list.
def cast_list(val):
    # Check if the input 'val' is an instance of a tuple, list, set, or dictionary.
    if isinstance(val, (tuple, list, set, dict)):
        # If 'val' is one of these types, convert it to a list and return.
        return list(val)
    else:	
        # If 'val' is not in the specified types, create a new list containing 'val' and return it.
        return [val]

# Create a sample list 'd1' containing one integer element.
d1 = [1]
# Print the type of 'd1' (which should be list) and the result of calling 'cast_list' on 'd1'.
print(type(d1))
print(cast_list(d1))

# Create a sample tuple 'd2' containing two string elements.
d2 = ('Red', 'Green')
# Print the type of 'd2' (which should be tuple) and the result of calling 'cast_list' on 'd2'.
print(type(d2))
print(cast_list(d2))

# Create a sample set 'd3' containing two string elements.
d3 = {'Red', 'Green'}
# Print the type of 'd3' (which should be set) and the result of calling 'cast_list' on 'd3'.
print(type(d3))
print(cast_list(d3))

# Create a sample dictionary 'd4' containing key-value pairs.
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
# Print the type of 'd4' (which should be dict) and the result of calling 'cast_list' on 'd4'.
print(type(d4))
print(cast_list(d4)) 

