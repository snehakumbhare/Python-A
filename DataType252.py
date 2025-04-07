#Python: Find the n minimum elements from the provided list

#Write a Python program to get the n minimum elements from a given list of numbers.

#Use sorted() to sort the list.

#Use slice notation to get the specified number of elements.
#Omit the second argument, n, to get a one-element list.
#If n is greater than or equal to the provided list's length, then return the original list (sorted in ascending order).
# Define a function 'min_n_nums' that takes a list 'nums' and an optional parameter 'n' (defaulting to 1).
# The function sorts the 'nums' list in ascending order and returns the top 'n' minimum values.
def min_n_nums(nums, n=1):
    return sorted(nums, reverse=False)[:n]

# Example 1: Create a list 'nums' with elements [1, 2, 3].
nums = [1, 2, 3]
print("Original list elements:")
print(nums)
# Call 'min_n_nums' to find the minimum value in the list.
print("Minimum values of the said list:", min_n_nums(nums))

# Example 2: Create another list 'nums' with elements [1, 2, 3].
nums = [1, 2, 3]
print("\nOriginal list elements:")
print(nums)
# Call 'min_n_nums' with 'n=2' to find the top two minimum values in the list.
print("Two minimum values of the said list:", min_n_nums(nums, 2))

# Example 3: Create a list 'nums' with negative and zero values.
nums = [-2, -3, -1, -2, -4, 0, -5]
print("\nOriginal list elements:")
print(nums)
# Call 'min_n_nums' with 'n=3' to find the top three minimum values in the list.
print("Three minimum values of the said list:", min_n_nums(nums, 3))

# Example 4: Create a list 'nums' with floating-point values.
print("\nOriginal list elements:")
nums = [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
print(nums)
# Call 'min_n_nums' with 'n=2' to find the top two minimum values in the list.
print("Two minimum values of the said list:", min_n_nums(nums, 2)) 
