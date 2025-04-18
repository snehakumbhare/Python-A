#Python: Moves the specified amount of elements to the start of the list

#Write a Python program to move the specified number of elements to the start of the given list.

#Use slice notation to get the two slices of the list and combine them before returning.

# Define a function named 'move_start' that moves elements of a list by a given 'offset.'
def move_start(nums, offset):
    return nums[-offset:] + nums[:-offset]
    # Slices the list from the negative 'offset' position to the end (equivalent to moving 
    #elements from the end to the start) and concatenates it with the portion from the start to the negative 'offset' position.

# Test the 'move_start' function with different lists and offsets.
print(move_start([1, 2, 3, 4, 5, 6, 7, 8], 3))
# Move the elements three positions to the start. (Expected output: [6, 7, 8, 1, 2, 3, 4, 5])

print(move_start([1, 2, 3, 4, 5, 6, 7, 8], -3))
# Move the elements three positions to the end. (Expected output: [4, 5, 6, 7, 8, 1, 2, 3])

print(move_start([1, 2, 3, 4, 5, 6, 7, 8], 8))
# The 'offset' equals the length of the list, resulting in the same list.

print(move_start([1, 2, 3, 4, 5, 6, 7, 8], -8))
# The negative 'offset' equals the negative length of the list, resulting in the same list.

print(move_start([1, 2, 3, 4, 5, 6, 7, 8], 7))
# Move the elements seven positions to the start. (Expected output: [2, 3, 4, 5, 6, 7, 8, 1])

print(move_start([1, 2, 3, 4, 5, 6, 7, 8], -7))
# Move the elements seven positions to the end. (Expected output: [8, 1, 2, 3, 4, 5, 6, 7]) 

