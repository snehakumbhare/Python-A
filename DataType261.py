#Python: Move given number of elements to the end of the list
#Write a Python program to move the specified number of elements to the end of the given list.

#Use slice notation to get the two slices of the list and combine them before returning
# Define a function named 'move_end' that moves elements of a list by a given 'offset.'
def move_end(nums, offset):
    return nums[offset:] + nums[:offset]
    # Slices the list from the 'offset' position to the end and concatenates it with the portion from the start to the 'offset' position.

# Test the 'move_end' function with different lists and offsets.
print(move_end([1, 2, 3, 4, 5, 6, 7, 8], 3))
# Move the elements three positions to the end. (Expected output: [4, 5, 6, 7, 8, 1, 2, 3])

print(move_end([1, 2, 3, 4, 5, 6, 7, 8], -3))
# Move the elements three positions to the beginning. (Expected output: [6, 7, 8, 1, 2, 3, 4, 5])

print(move_end([1, 2, 3, 4, 5, 6, 7, 8], 8))
# The 'offset' equals the length of the list, resulting in the same list.

print(move_end([1, 2, 3, 4, 5, 6, 7, 8], -8))
# The negative 'offset' equals the negative length of the list, resulting in the same list.

print(move_end([1, 2, 3, 4, 5, 6, 7, 8], 7))
# Move the elements seven positions to the end. (Expected output: [2, 3, 4, 5, 6, 7, 8, 1])

print(move_end([1, 2, 3, 4, 5, 6, 7, 8], -7))
# Move the elements seven positions to the beginning. (Expected output: [8, 1, 2, 3, 4, 5, 6, 7])
