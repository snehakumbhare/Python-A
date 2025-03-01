#Python: Find the index of the last element in the given list that satisfies a testing function

#Write a  Python program to find the index of the last element in the given list that satisfies the provided  testing function.
# Define a function 'find_last_index' that takes a list 'lst' and a function 'fn' as input.
def find_last_index(lst, fn):
    # Reverse the 'lst', enumerate it, and find the first index where the function 'fn' returns 'True' in the reversed list.
    # Then, subtract the found index from the length of the list to get the last index where 'fn' returned 'True' in the original list.
    return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))

# Call the 'find_last_index' function with an example list and a lambda function 'fn', and print the result.
print(find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1))
