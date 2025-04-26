#Python: Check if the elements of the first list are contained in the second one regardless of order

#Write a Python program to check if the elements of the first list are contained in the second one regardless of order.

#Use count() to check if any value in a has more occurrences than it has in b.

#Return False if any such value is found, True otherwise.

# Define a function named 'is_contained_in' to check if all elements in l1 are contained in l2.

# It takes two parameters: 'l1' (the first list) and 'l2' (the second list).
def is_contained_in(l1, l2):
    # Iterate through the set of unique elements in l1.
    for x in set(l1):
        # Check if the count of the element in l1 is greater than the count in l2.
        if l1.count(x) > l2.count(x):
            # If any element is more frequent in l1 than in l2, return False.
            return False
    # If all elements in l1 are contained in l2, return True.
    return True

# Test the 'is_contained_in' function with different lists.
print(is_contained_in([1, 2], [2, 4, 1]))  # Check if [1, 2] is contained in [2, 4, 1].
print(is_contained_in([1], [2, 4, 1]))  # Check if [1] is contained in [2, 4, 1].
print(is_contained_in([1, 1], [4, 2, 1]))  # Check if [1, 1] is contained in [4, 2, 1].
print(is_contained_in([1, 1], [3, 2, 4, 1, 5, 1]))  # Check if [1, 1] is contained in [3, 2, 4, 1, 5, 1]. 
