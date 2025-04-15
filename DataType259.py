#Python: Check if all the elements in values are included in another given list

#Write a Python program to check if all the elements of a list are included in another given list.

#Check if every value in lsts is contained in nums using a for loop.

#Return False if any one value is not found, True otherwise.
# Define a function named 'test_includes_all' that checks if all elements in a list are included in another list.
def test_includes_all(nums, lsts):
    for x in lsts:
        if x not in nums:
            return False
            # If any element 'x' in 'lsts' is not found in 'nums', return False.
    return True
    # If all elements in 'lsts' are found in 'nums', return True.

# Test the 'test_includes_all' function with different lists.
print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 40]))
# Check if all elements in the second list are included in the first list. (Expected output: True)

print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 80]))
# Check if all elements in the second list are included in the first list. (Expected output: False)
