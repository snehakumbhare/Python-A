#Python: Chunk a given list into smaller lists of a specified size
#Write a  Python program to chunk a given list into smaller lists of a specified size.

#Use list() and range() to create a list of the desired size.
#Use map() on the list and fill it with splices of the given list.
#Finally, return the created list.
# Import the 'ceil' function from the 'math' module.
from math import ceil

# Define a function 'chunk_list' that takes a list 'lst' and an integer 'size' as input.
def chunk_list(lst, size):
    # Use list comprehensions to create a list of chunks, where each chunk has 'size' elements.
    # The 'range' function is used to generate the indices for splitting the list.
    return list(map(lambda x: lst[x * size:x * size + size],  # Lambda function to get each chunk.
            list(range(ceil(len(lst) / size)))))  # Calculate the number of chunks needed and generate indices.

# Call the 'chunk_list' function with an example list and chunk size.
print(chunk_list([1, 2, 3, 4, 5, 6, 7, 8], 3))

