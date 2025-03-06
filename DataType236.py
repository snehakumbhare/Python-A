#Python: Convert a list of dictionaries into a list of values corresponding to the specified key
#Write a  Python program to convert a given list of dictionaries into a list of values corresponding to the specified key.

#Use a list comprehension and dict.get() to get the value of key for each dictionary in lst.
# Define a function 'pluck' that takes a list 'lst' and a key 'key' as input.
def pluck(lst, key):
    # Use a list comprehension to iterate through the dictionaries 'x' in the list 'lst'.
    # For each dictionary 'x', get the value associated with the 'key' using the 'get' method.
    # Return a list of these values.
    return [x.get(key) for x in lst]

# Create a list of dictionaries 'simpsons' with 'name' and 'age' keys.
simpsons = [
    { 'name': 'Areeba', 'age': 8 },
    { 'name': 'Zachariah', 'age': 36 },
    { 'name': 'Caspar', 'age': 34 },
    { 'name': 'Presley', 'age': 10 }
]

# Call the 'pluck' function with the list 'simpsons' and the key 'age', and print the result.
print(pluck(simpsons, 'age'))
