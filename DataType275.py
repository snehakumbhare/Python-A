#Python Exercises: Find the largest odd number in a list of integers

#Write a Python program to find the largest odd number in a given list of integers.
# Define a function named 'test' that takes a list 'nums' as input.
def test(nums):
    # Use a list comprehension to filter out odd numbers (numbers not divisible by 2) from the input list 'nums'.
    odd_nums = [x for x in nums if x % 2 != 0]
    
    # Check if the list 'odd_nums' is empty, meaning there are no odd numbers in the 'nums' list.
    if len(odd_nums) == 0:
        # If there are no odd numbers, return -1 as a sentinel value to indicate no odd numbers were found.
        return -1
    else:
        # If there are odd numbers, find and return the maximum (largest) odd number in the 'odd_nums' list.
        return max(odd_nums)

# Define the original list 'nums'.
nums = [0, 9, 2, 4, 5, 6]
print("Original list:")
print(nums)
# Call the 'test' function to find the largest odd number in the list.
print("Find the largest odd number in the said list:", test(nums))

# Define another list 'nums'.
nums = [-4, 0, 6, 1, 0, 2]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the second list of numbers.
print("Find the largest odd number in the said list:", test(nums))

# Define another list 'nums'.
nums = [1, 2, 3]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the third list of numbers.
print("Find the largest odd number in the said list:", test(nums))

# Define another list 'nums'.
nums = [-4, 0, 5, 1, 0, 1]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the fourth list of numbers.
print("Find the largest odd number in the said list:", test(nums)) 

