#Python: Generates a list of numbers in the arithmetic progression within a range

#Write a Python program to generate a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.

 # Define a function named 'arithmetic_progression' to generate a list of numbers in an arithmetic progression.

# It takes two parameters: 'n' is the starting number, and 'x' is the end number.
def arithmetic_progression(n, x):
    # Use the 'range' function to generate a list of numbers from 'n' to 'x' (inclusive) with a step size of 'n'.
    return list(range(n, x + 1, n))

# Call the 'arithmetic_progression' function to generate an arithmetic progression starting from 1 to 15 with a step of 1.
print(arithmetic_progression(1, 15))
# Call the function to generate an arithmetic progression starting from 3 to 37 with a step of 3.
print(arithmetic_progression(3, 37))
# Call the function to generate an arithmetic progression starting from 5 to 25 with a step of 5.
print(arithmetic_progression(5, 25))

