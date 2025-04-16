#Python: Most frequent element in a given list of numbers

#Write a Python program to get the most frequent element in a given list of numbers.

#Use set() to get the unique values in nums.
#Use max() to find the element that has the most appearances.
# Define a function named 'most_frequent' that finds the most frequently occurring item in a list.
def most_frequent(nums):
    return max(set(nums), key=nums.count)
    # Using 'set' to remove duplicates, then finding the item with the maximum count using the 'max' function.

# Test the 'most_frequent' function with different lists.
print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))
# Find the most frequently occurring item in the list. (Expected output: 2)

nums = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
print("Original list:")
print(nums)
print("Item with the maximum frequency of the said list:")
print(most_frequent(nums))
# Find the most frequently occurring item in the list.

nums = [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
print("\nOriginal list:")
print(nums)
print("Item with the maximum frequency of the said list:")
print(most_frequent(nums))
# Find the most frequently occurring item in the list. 
