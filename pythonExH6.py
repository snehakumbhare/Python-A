#Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
# Try to execute the following block of code, which may raise exceptions.

# Prompt the user to input a number and attempt to convert it to an integer, storing it in the 'n' variable.
try:
    n = int(input("Input a number: "))
    # If the user input is successfully converted to an integer, print the entered number.
    print("You entered:", n)
# Handle the KeyboardInterrupt exception, which occurs when the user cancels the input (typically by pressing Ctrl+C).
except KeyboardInterrupt:
    print("Input canceled by the user.")
