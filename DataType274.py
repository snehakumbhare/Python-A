#Python Exercises: Sum of all list elements except current element
#Write a Python program to add all elements of a list of integers except the number at index. Return the updated string.
# Define a function named 'test' that takes a list 'nums' as input.
def test(nums):
    # Use a list comprehension to calculate the sum of all elements in the 'nums' list,
    # and then subtract each element 'x' from the total sum. This gives the sum of all elements except the current one.
    return [sum(nums) - x for x in nums]

# Define the original list 'nums'.
nums = [0, 9, 2, 4, 5, 6]
print("Original list:")
print(nums)
# Call the 'test' function to calculate the sum of elements except the current element for each element in the list.
print("Sum of said list elements except the current element:\n", test(nums))

# Define another list 'nums'.
nums = [-4, 0, 6, 1, 0, 2]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the second list of numbers.
print("Sum of said list elements except the current element:\n", test(nums))

# Define another list 'nums'.
nums = [1, 2, 3]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the third list of numbers.
print("Sum of said list elements except the current element:\n", test(nums))

# Define another list 'nums'.
nums = [-4, 0, 5, 1, 0, 1]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the fourth list of numbers.
print("Sum of said list elements except the current element:\n", test(nums))

