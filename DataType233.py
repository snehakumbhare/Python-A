#Python: Convert a given number (integer) to a list of digits
#Write a Python program to convert a given number (integer) to a list of digits.

#Use map() combined with int on the string representation of n and return a list from the result.

# Define a function 'digitize' that takes an integer 'n' as input.
def digitize(n):
    # Convert the integer 'n' to a string, map each character to an integer, and create a list of those integers.
    return list(map(int, str(n)))

# Call the 'digitize' function with example integers and print the results.
print(digitize(123))
print(digitize(1347823)) 
