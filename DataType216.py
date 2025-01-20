#Python: Split values into two groups, based on the result of the given filtering function

#Write a Python program to split values into two groups, based on the result of the given filtering function.

#Use a list comprehension to add elements to groups, based on the value returned by fn for each element.
#If fn returns a truthy value for any element, add it to the first group, otherwise add it to the second group
# Define a function called 'bifurcate_by' that splits a list into two sublists based on a provided function.
def bifurcate_by(lst, fn):
    # Create two sublists: one with elements that satisfy the condition (fn(x) is True),
    # and the other with elements that do not satisfy the condition (fn(x) is False).
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]

# Example usage: Split a list into two sublists based on whether the elements start with 'w'.
print(bifurcate_by(['red', 'green', 'black', 'white'], lambda x: x[0] == 'w')) 
