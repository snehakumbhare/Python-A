#Python: Check if a given function returns True for every element in a list
#Write a Python program to check if a given function returns True for every element in a list.

#Use all() in combination with map() and fn to check if fn returns True for all elements in the list.
# Define a function 'every' that takes a list 'lst' and an optional function 'fn' as input.
# The default function 'fn' is set to an identity function.
def every(lst, fn=lambda x: x):
    # Use the 'all' function to check if every element in the list 'lst' satisfies the condition specified by 'fn'.
    return all(map(fn, lst))
	
# Call the 'every' function with different lists and conditions, and print the results.
print(every([4, 2, 3], lambda x: x > 1))
print(every([4, 2, 3], lambda x: x < 1))
print(every([4, 2, 3], lambda x: x == 1)) 
