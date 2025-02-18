#Python: Split values into two groups, based on the result of the given filter list

#Write a  Python program to split values into two groups, based on the result of the given filter list.

#Use a list comprehension and zip() to add elements to groups, based on filter.

#If filter has a truthy value for any element, add it to the first group, otherwise add it to the second group.
# Define a function 'bifurcate' that takes a list 'colors' and a list of filters 'filter' as input.
def bifurcate(colors, filter):
    # Use list comprehensions to create two lists: one with elements corresponding to True filter values and one with elements corresponding to False filter values.
    return [
        [x for x, flag in zip(colors, filter) if flag],
        [x for x, flag in zip(colors, filter) if not flag]
    ]

# Call the 'bifurcate' function with example lists 'colors' and 'filter'.
print(bifurcate(['red', 'green', 'blue', 'pink'], [True, True, False, True]))
