#Python: Minimum value of a list, after mapping each element to a value using a giving function
#Write a Python program to get the minimum value of a list, after mapping each element to a value using a given function.

#Use map() with fn to map each element to a value using the provided function.
#Use min() to return the minimum value.
# Define a function 'min_by' that takes a list 'lst' and a function 'fn'.
# It uses the 'min' function to find the minimum value in 'lst' based on the results of applying 'fn' to each element.
def min_by(lst, fn):
    return min(map(fn, lst))

# Call the 'min_by' function with a list of dictionaries and a lambda function.
# The lambda function extracts the 'n' value from each dictionary.
# The function returns the minimum 'n' value from the list of dictionaries.
print(min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))
