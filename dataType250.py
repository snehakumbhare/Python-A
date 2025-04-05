#Python: Initialize and fills a list with the specified value
#Write a Python program that fills a list with the specified value.

#Use a list comprehension and range() to generate a list of length equal to n, filled with the desired values.
#Omit val to use the default value of 0.
# Define a function 'initialize_list_with_values' that takes two arguments, 'n' and 'val'.
# The function creates a list containing 'n' elements, each initialized with the value 'val'.
def initialize_list_with_values(n, val=0):
    return [val for x in range(n)]

# Call the 'initialize_list_with_values' function with different arguments to create lists.
# Example 1: Create a list with 7 elements, all initialized with the default value 0.
print(initialize_list_with_values(7))

# Example 2: Create a list with 8 elements, all initialized with the value 3.
print(initialize_list_with_values(8, 3))

# Example 3: Create a list with 5 elements, all initialized with the value -2.
print(initialize_list_with_values(5, -2))

# Example 4: Create a list with 5 elements, all initialized with the value 3.2.
print(initialize_list_with_values(5, 3.2))
