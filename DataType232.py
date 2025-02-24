#Python: Chunk a given list into n smaller lists

#Write a Python program to chunk a given list into n smaller lists.

#Use math.ceil() and len() to get the size of each chunk.

#Use list() and range() to create a new list of size n.

#Use map() to map each element of the new list to a chunk the length of size.
#If the original list can't be split evenly, the final chunk will contain the remaining elements.
# Import the 'ceil' function from the 'math' module.
from math import ceil

# Define a function 'chunk_list_into_n' that takes a list 'nums' and an integer 'n' as input.
def chunk_list_into_n(nums, n):
    # Calculate the size of each chunk based on the length of the list and the number of chunks (n).
    size = ceil(len(nums) / n)
    
    # Use list comprehensions to create a list of chunks, where each chunk has 'size' elements.
    # The 'range' function is used to generate the indices for splitting the list.
    return list(map(lambda x: nums[x * size:x * size + size],  # Lambda function to get each chunk.
                  list(range(n))))  # Generate 'n' indices for chunking the list.

# Call the 'chunk_list_into_n' function with an example list and the number of chunks.
print(chunk_list_into_n([1, 2, 3, 4, 5, 6, 7], 4))    
