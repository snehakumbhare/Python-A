#Handling TypeError Exception in Python numeric input program

#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
# Define a function named get_numeric_input that takes a prompt as a parameter.
def get_numeric_input(prompt):
    # Use a while loop to repeatedly prompt the user until a valid numeric input is provided.
    while True:
        try:
            # Attempt to get a numeric input (float) from the user and store it in the 'value' variable.
            value = float(input(prompt))
            # Return the numeric value.
            return value
        except ValueError:
            # Handle the exception if the user's input is not a valid number.
            print("Error: Invalid input. Please Input a valid number.")

# Usage
# Call the get_numeric_input function to get the first numeric input from the user with the provided prompt.
n1 = get_numeric_input("Input the first number: ")
# Call the get_numeric_input function to get the second numeric input from the user with the provided prompt.
n2 = get_numeric_input("Input the second number: ")
# Calculate the product of the two input numbers.
result = n1 * n2
# Print the result, which is the product of the two numbers.
print("Product of the said two numbers:", result)
