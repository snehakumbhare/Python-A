#Python: Check if two lists contain the same elements regardless of order

#Write a Python program to check if two given lists contain the same elements regardless of order.

#Use set() on the combination of both lists to find the unique values.

#Iterate over them with a for loop comparing the count() of each unique value in each list.

#Return False if the counts do not match for any element, True otherwise.

# Define a function to check if two lists contain the same elements regardless of order.
def check_same_contents(nums1, nums2):
    # Loop through the set of elements in the combined lists.
    for x in set(nums1 + nums2):
        # Check if the count of element 'x' in nums1 is not equal to the count of 'x' in nums2.
        if nums1.count(x) != nums2.count(x):
            return False  # If counts are not equal, the lists do not have the same contents.
    return True  # If all counts are equal for all elements, the lists have the same contents.
	
# Example 1
nums1 = [1, 2, 4]
nums2 = [2, 4, 1]
print("Original list elements:")
print(nums1)
print(nums2)
print("\nCheck two said lists contain the same elements regardless of order!")
print(check_same_contents(nums1, nums2))

# Example 2
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print("\nOriginal list elements:")
print(nums1)
print(nums2)
print("\nCheck two said lists contain the same elements regardless of order!")
print(check_same_contents(nums1, nums2))

# Example 3
nums1 = [1, 2, 3]
nums2 = [1, 2, 4]
print("\nOriginal list elements:")
print(nums1)
print(nums2)
print("\nCheck two said lists contain the same elements regardless of order!")
print(check_same_contents(nums1, nums2)) 
