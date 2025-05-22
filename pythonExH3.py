#Handling FileNotFoundError Exception in Python File Handling Program
#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# Define a function named open_file that takes a filename as a parameter.
def open_file(filename):
    try:
        # Attempt to open the specified file in read mode ('r').
        file = open(filename, 'r')
        # Read the contents of the file and store them in the 'contents' variable.
        contents = file.read()
        # Print a message to indicate that the file contents will be displayed.
        print("File contents:")
        # Print the contents of the file.
        print(contents)
        # Close the file to release system resources.
        file.close()
    except FileNotFoundError:
        # Handle the exception if the specified file is not found.
        print("Error: File not found.")

# Usage
# Prompt the user to input a file name and store it in the 'file_name' variable.
file_name = input("Input a file name: ")
# Call the open_file function with the provided file name.
open_file(file_name) 
