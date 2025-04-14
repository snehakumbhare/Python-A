#Python: Check if a given function returns True for at least one element in the list

#Write a Python program to check if a given function returns True for at least one element in the list.

#Use all() and fn to check if fn returns False for all the elements in the list.

# Define a function named 'test' that checks whether a condition is False for all elements in a list.
def test(lst, fn=lambda x: x):
    return all(not fn(x) for x in lst)
    # The 'all' function checks if the given condition 'not fn(x)' is False for all elements in the list 'lst'.

# Test the 'test' function with different lists and conditions.
print(test([1, 0, 2, 3], lambda x: x >= 3))
# Check if all elements are less than 3. (Expected output: False)

print(test([1, 0, 2, 3], lambda x: x < 0))
# Check if all elements are less than 0. (Expected output: False)

print(test([2, 2, 4, 4]))
# Check if all elements are False (considering default condition of 'x').
# Since there are no False elements, the expected output is True.
