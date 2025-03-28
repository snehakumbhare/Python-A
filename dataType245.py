#Python: Check if a given function returns True for at least one element in the list
#Write a Python program to check if a given function returns True for at least one element in the list.

#Use any() in combination with map() to check if fn returns True for any element in the list.
# Define a function 'some' that takes a list 'lst' and an optional function 'fn'.
# It uses the 'any' function and 'map' to check if any element in the list satisfies the given condition specified by 'fn'.
def some(lst, fn=lambda x: x):
    return any(map(fn, lst))
	
# Call the 'some' function with different lists and conditions, and print the results.
print(some([0, 1, 2, 0], lambda x: x >= 2))
print(some([5, 10, 20, 10], lambda x: x < 2)) 
