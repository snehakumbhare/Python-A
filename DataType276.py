#Python Exercises: Largest, lowest gap between sorted values of a list

#Write a Python program to calculate the largest and smallest gap between sorted elements of a list of integers.
# Define a function named 'test' that takes a list 'nums' as input.
def test(nums):
    # Sort the elements in the input list 'nums' in ascending order.
    nums.sort()
    
    # Calculate the largest gap between consecutive sorted values and store it in 'max_gap'.
    max_gap = max(b - a for a, b in zip(nums, nums[1:]))
    
    # Calculate the smallest gap between consecutive sorted values and store it in 'min_gap'.
    min_gap = min(b - a for a, b in zip(nums, nums[1:]))
    
    # Return a tuple containing both the 'max_gap' and 'min_gap'.
    return max_gap, min_gap

# Define the original list 'nums'.
nums = [0, 9, 2, 4, 5, 6]
print("Original list:")
print(nums)
# Call the 'test' function to find the largest and smallest gap between sorted values in the list.
print("Largest, lowest gap between sorted values of the said list:", test(nums))

# Define another list 'nums'.
nums = [23, -2, 45, 38, 12, 4, 6]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the second list of numbers.
print("Largest, lowest gap between sorted values of the said list:", test(nums))

# Define another list 'nums'.
nums = [1, 2, 3]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the third list of numbers.
print("Largest, lowest gap between sorted values of the said list:", test(nums))

# Define another list 'nums'.
nums = [-4, -3, 5, 20, 10, 1]
print("\nOriginal list:")
print(nums)
# Call the 'test' function for the fourth list of numbers.
print("Largest, lowest gap between sorted values of the said list:", test(nums)) 

