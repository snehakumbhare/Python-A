#Python: Sort a given list of strings(numbers) numerically
#Write a  Python program to sort a given list of strings(numbers) numerically.
# Define a function 'sort_numeric_strings' that sorts a list of numeric strings numerically
def sort_numeric_strings(nums_str):
    # Convert each numeric string to an integer and store the result in 'result'
    result = [int(x) for x in nums_str]
    # Sort the 'result' list in ascending order
    result.sort()
    return result

# Create a list of numeric strings 'nums_str'
nums_str = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums_str'
print(nums_str)

# Sort the list of numeric strings numerically using the 'sort_numeric_strings' function
print("\nSort the said list of strings (numbers) numerically:")
# Call the 'sort_numeric_strings' function with 'nums_str', then print the result
print(sort_numeric_strings(nums_str)) 
