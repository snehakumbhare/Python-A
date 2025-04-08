#Python: Find the weighted average of two or more numbers

#Write a Python program to get the weighted average of two or more numbers.

# Define a function 'weighted_average' that takes two lists 'nums' and 'weights'.

# The function calculates the weighted average by summing the product of corresponding elements in 'nums' and 'weights'

# and dividing it by the sum of 'weights'.
def weighted_average(nums, weights):
    return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
	
# Example 1: Create two lists 'nums1' and 'nums2' with elements.
nums1 = [10, 50, 40]
nums2 = [2, 5, 3]
print("Original list elements:")
print(nums1)
print(nums2)
# Call 'weighted_average' to compute the weighted average of 'nums1' and 'nums2'.
print("\nWeighted average of the said two lists of numbers:")
print(weighted_average(nums1, nums2))

# Example 2: Create two lists 'nums1' and 'nums2' with elements.
nums1 = [82, 90, 76, 83]
nums2 = [.2, .35, .45, 32]
print("\nOriginal list elements:")
print(nums1)
print(nums2)
# Call 'weighted_average' to compute the weighted average of 'nums1' and 'nums2'.
print("\nWeighted average of the said two lists of numbers:")
print(weighted_average(nums1, nums2)) 
