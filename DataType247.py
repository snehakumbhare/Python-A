#Python: Maximum value of a list, after mapping each element to a value using a giving function

#Write a Python program to get the maximum value of a list, after mapping each element to a value using a given function.

#Use map() with fn to map each element to a value using the provided function.
#Use max() to return the maximum value.
# Define a function 'max_by' that takes a list 'lst' and a function 'fn'.
# It uses the 'max' function to find the maximum value in 'lst' based on the results of applying 'fn' to each element.
def max_by(lst, fn):
    return max(map(fn, lst))

# Call the 'max_by' function with a list of dictionaries and a lambda function.
# The lambda function extracts the 'n' value from each dictionary.
# The function returns the maximum 'n' value from the list of dictionaries.
print(max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))
