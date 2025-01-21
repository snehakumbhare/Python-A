#Python: Sort one list based on another list containing the desired indexes

#Write a Python program to sort one list based on another list containing the desired indexes.

#Use zip() and sorted() to combine and sort the two lists, based on the values of indexes.
#Use a list comprehension to get the first element of each pair from the result
#Use the reverse parameter in sorted() to sort the dictionary in reverse order, based on the third argument
# Define a function called 'sort_by_indexes' that sorts a list based on a list of corresponding indexes.
def sort_by_indexes(lst, indexes, reverse=False):
    # Use the 'sorted' function to sort the list 'lst' based on the corresponding indexes.
    # The 'zip' function is used to pair each element of 'indexes' with the elements of 'lst'.
    # The sorting is done based on the indexes, and the 'reverse' flag determines whether to sort in reverse order.
    return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: x[0], reverse=reverse)]

# Example usage: Sort 'l1' based on the corresponding indexes in 'l2'.
l1 = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
l2 = [3, 2, 6, 4, 1, 5]
print(sort_by_indexes(l1, l2))  # Sort in ascending order.
print(sort_by_indexes(l1, l2, True))  # Sort in descending order. 
