#Python: Find the longest one from any number of iterable objects or objects with a length property
#Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.

#Use max() with len() as the key to return the item with the greatest length.
#If multiple objects have the same length, the first one will be returned.
# Define a function 'longest_item' that takes a variable number of arguments (*args).
# It returns the argument with the maximum length using the 'max' function and 'len' as the key function.
def longest_item(*args):
    return max(args, key=len)

# Call the 'longest_item' function with different arguments and print the results.
print(longest_item('this', 'is', 'a', 'Green'))
print(longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))
print(longest_item([1, 2, 3, 4], 'Red')) 
