#Python: Create a list with the non-unique values filtered out

#Write a  Python program to create a list with non-unique values filtered out.

#Use collections.Counter to get the count of each value in the list.
#Use a list comprehension to create a list containing only the unique values.
# Import the 'Counter' class from the 'collections' module.

from collections import Counter

# Define a function called 'filter_non_unique' that takes a list 'lst' as an argument.
def filter_non_unique(lst):
  # Create a list of items and their corresponding counts using the 'Counter' class.
  # Filter this list to include only items with a count of 1.
  return [item for item, count in Counter(lst).items() if count == 1]

# Example: Filter out non-unique elements from a list.
print(filter_non_unique([1, 2, 2, 3, 4, 4, 5]))

