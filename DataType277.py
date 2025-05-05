#dismiss
#Python Exercises: Sum of missing numbers of a list of integers
#Write a Python program to sum the missing numbers in a given list of integers
# Define a function named 'test' that takes a list 'nums' as input.
def test(nums):
    # Find the maximum and minimum numbers in the input list 'nums'.
    max_num = max(nums)
    min_num = min(nums)
    
    # Calculate the sum of missing numbers within the range [min_num, max_num] using the formula:
    # Sum = (max + min) * (max - min + 1) // 2 - sum(nums)
    return (max_num + min_num) * (max_num - min_num + 1) // 2 - sum(nums)

# Define the original list 'nums'.
nums = [0, 3, 4, 7, 9]
print("Original list:")
print(nums)

# Call the 'test' function to calculate the sum of missing numbers in the list of integers.
print("Sum of missing numbers of the said list of integers:", test(nums))

# Define another list 'nums'.
nums = [44, 45, 48]
print("\nOriginal list:")
print(nums)

# Call the 'test' function for the second list of integers.
print("Sum of missing numbers of the said list of integers:", test(nums))

# Define another list 'nums'.
nums = [-7, -5, -4, 0]
print("\nOriginal list:")
print(nums)

# Call the 'test' function for the third list of integers.
print("Sum of missing numbers of the said list of integers:", test(nums)) 
