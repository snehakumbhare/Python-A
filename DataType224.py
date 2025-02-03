#Python: Retrieve the value of the nested key indicated by the given selector list from a dictionary or list

#Write a  Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.

#Use functools.reduce() to iterate over the selectors list.

#Apply operator.getitem() for each key in selectors, retrieving the value to be used as the iteratee for the next iteration.
# Import the 'reduce' function from the 'functools' module and the 'getitem' function from the 'operator' module.
from functools import reduce 
from operator import getitem

# Define a function called 'get' that takes a dictionary 'd' and a list of 'selectors'.
def get(d, selectors):
  # Use the 'reduce' function to access nested dictionary values by applying 'getitem' successively.
  return reduce(getitem, selectors, d) 

# Create a nested dictionary 'users' with user information.
users = {
  'freddy': {
    'name': {
      'first': 'Fateh',
      'last': 'Harwood' 
    },
    'postIds': [1, 2, 3]
  }
}

# Example: Access values in the 'users' dictionary using nested selectors.
print(get(users, ['freddy', 'name', 'last']))
print(get(users, ['freddy', 'postIds', 1])) 
