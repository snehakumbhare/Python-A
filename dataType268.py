#Python: Get every nth element in a given list

#Write a Python program to get every nth element in a given list.

#Use slice notation to create a new list that contains every nth element of the given list
# Define a function named 'every_nth' that returns every nth element from a list.
# It takes two parameters: 'nums' (the list) and 'nth' (the interval for selecting elements).
def every_nth(nums, nth):
    # Use list slicing to return elements starting from the (nth-1) index, with a step of 'nth'.
    return nums[nth - 1::nth]

# Create a sample list of integers from 1 to 10.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print the original list elements.
print(every_nth(nums, 1))  # Select every 1st element (no change).
print(every_nth(nums, 2))  # Select every 2nd element.
print(every_nth(nums, 5))  # Select every 5th element.
print(every_nth(nums, 6))  # Select every 6th element. 
