#Python: Randomize the order of the values of an list
#Write a  Python program to randomize the order of the values of a list, returning a new list.

#Uses the Fisher-Yates algorithm to reorder the elements of the list.
#random.shuffle provides similar functionality to this snippet.
# Import necessary modules.
from copy import deepcopy
from random import randint

# Define a function called 'shuffle_list' that takes a list 'lst' as an argument.
def shuffle_list(lst):
  # Create a deep copy of the input list to avoid modifying the original list.
  temp_lst = deepcopy(lst)
  # Get the length of the copied list.
  m = len(temp_lst)
  # Perform Fisher-Yates shuffle by iterating over the list and swapping elements randomly.
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  # Return the shuffled list.
  return temp_lst

# Example usage: Shuffle the elements of the list 'nums'.
nums = [1, 2, 3, 4, 5, 6]
print("Original list: ", nums)
print("\nShuffle the elements of the said list:")
print(shuffle_list(nums)) 
