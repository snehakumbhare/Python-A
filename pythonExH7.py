#Handling ArithmeticError exception in Python division program
#Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
# Define a function named 'division' that takes 'dividend' and 'divisor' as parameters.
def division(dividend, divisor):
    try:
        # Try to perform the division operation and store the result in the 'result' variable.
        result = dividend / divisor
        # Print the result of the division.
        print("Result:", result)
    except ArithmeticError:
        # Handle the exception if an ArithmeticError occurs during the division operation.
        print("Error: Arithmetic error occurred!")

# Usage

# Prompt the user to input the dividend and store it as a floating-point number in the 'dividend' variable.
dividend = float(input("Input the dividend: "))
# Prompt the user to input the divisor and store it as a floating-point number in the 'divisor' variable.
divisor = float(input("Input the divisor: "))
# Call the 'division' function with the provided dividend and divisor.
division(dividend, divisor) 

