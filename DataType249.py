#Python: Calculate the sum of a list, after mapping each element to a value using a given function

#Write a Python program to calculate the sum of a list, after mapping each element to a value using the provided function.

#Use map() with fn to map each element to a value using the provided function.
#Use sum() to return the sum of the values.
# Define a function 'sum_by' that takes a list 'lst' and a function 'fn'.
# It calculates the sum of the values obtained by applying 'fn' to each element in the list.
def sum_by(lst, fn):
    return sum(map(fn, lst))

# Call the 'sum_by' function with a list of dictionaries and a lambda function.
# The lambda function extracts the 'n' value from each dictionary.
# The function returns the sum of all 'n' values from the list of dictionaries.
print(sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))
