#Python ZeroDivisionError Exception Handling

#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

## Define a function named divide_numbers that takes two parameters: x and y.
def divide_numbers(x, y):
    try:
        # Attempt to perform the division operation and store the result in the 'result' variable.
        result = x / y
        # Print the result of the division.
        print("Result:", result)
    except ZeroDivisionError:
        # Handle the exception if a division by zero is attempted.
        print("The division by zero operation is not allowed.")

# Usage
# Define the numerator and denominator values.
numerator = 100
denominator = 0
# Call the divide_numbers function with the provided numerator and denominator.
divide_numbers(numerator, denominator)
