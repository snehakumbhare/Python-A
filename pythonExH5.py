#Handling IndexError Exception in Python list operation program
#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
# Define a function named test_index that takes 'data' and 'index' as parameters.
def test_index(data, index):
    try:
        # Try to access an element at the specified 'index' in the 'data' list and store it in the 'result' variable.
        result = data[index]
        # Perform desired operation using the result (in this case, printing it).
        print("Result:", result)
    except IndexError:
        # Handle the exception if the specified 'index' is out of range for the 'data' list.
        print("Error: Index out of range.")

# Define a list of numbers 'nums'.
nums = [1, 2, 3, 4, 5, 6, 7]
# Prompt the user to input an index and store it in the 'index' variable.
index = int(input("Input the index: "))
# Call the test_index function with the 'nums' list and the user-provided 'index'.
test_index(nums, index)
