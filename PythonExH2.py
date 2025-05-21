#Handling ValueError Exception in Python integer input program

#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
# Define a function named get_integer_input that takes a prompt as a parameter.
def get_integer_input(prompt):
    try:
        # Attempt to get an integer input from the user and store it in the 'value' variable.
        value = int(input(prompt))
        # Return the integer value.
        return value
    except ValueError:
        # Handle the exception if the user's input is not a valid integer.
        print("Error: Invalid input, input a valid integer.")

# Usage
# Call the get_integer_input function to get an integer input from the user with the provided prompt.
n = get_integer_input("Input an integer: ")
# Print the input value obtained from the function.
print("Input value:", n)
