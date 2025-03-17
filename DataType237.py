#Python: Calculate the average of a given list, after mapping each element to a value using the provided function

#Write a Python program to calculate the average of a given list, after mapping each element to a value using the provided function.

#Use map() to map each element to the value returned by fn.
#Use sum() to sum all of the mapped values, divide by len(lst).
#Omit the last argument, fn, to use the default identity function.
# Define a function 'average_by' that takes a list 'lst' and an optional function 'fn' as input.
def average_by(lst, fn=lambda x: x):
    # Calculate the average of the values in the list 'lst' by performing the following steps:
    # 1. Use the 'map' function to apply the function 'fn' to each element of the list 'lst'.
    # 2. Use 'sum' to calculate the sum of the mapped values, starting with a floating-point 0.0.
    # 3. Divide the sum by the length of the list 'lst' to compute the average.
    return sum(map(fn, lst), 0.0) / len(lst)

# Call the 'average_by' function with a list of dictionaries and a lambda function to extract the 'n' key's value.
# Print the result, which is the average of the 'n' values.
print(average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']))
print(average_by([{ 'n': 10 }, { 'n': 20 }, { 'n': -30 }, { 'n': 60 }], lambda x: x['n'])) 
