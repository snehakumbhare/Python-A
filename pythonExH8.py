#Handling UnicodeDecodeError Exception in Python file Handling program

#Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

# Define a function named 'open_file' that takes 'filename' as a parameter.
def open_file(filename):
    # Prompt the user to input the file encoding (ASCII, UTF-16, UTF-8) and store it in the 'encoding' variable.
    encoding = input("Input the encoding (ASCII, UTF-16, UTF-8) for the file: ")
    try:
        # Attempt to open the file with the specified encoding in read mode and use the 'with' statement for automatic file closing.
        with open(filename, 'r', encoding=encoding) as file:
            # Read the contents of the file and store it in the 'contents' variable.
            contents = file.read()
            # Print the contents of the file.
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        # Handle the exception if a UnicodeDecodeError occurs during file reading due to an encoding issue.
        print("Error: Encoding issue occurred while reading the file.")

# Usage

# Prompt the user to input the file name and store it in the 'file_name' variable.
file_name = input("Input the file name: ")
# Call the 'open_file' function with the provided file name to open and read the file with the specified encoding.
open_file(file_name) 
