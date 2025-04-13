#Python: Create a given flat list of all the keys in a flat dictionary

#Write a Python program to create a flat list of all the keys in a flat dictionary.

#Use dict.keys() to return the keys in the given dictionary.
#Return a list() of the previous result.
# Define a function to extract and return a list of keys from a dictionary.
def keys_only(students):
    return list(students.keys())  # Use the keys() method to get the keys from the dictionary.

# Create a dictionary of students with names as keys and their respective grades as values.
students = {
    'Sachin': 10,
    'Raj': 11,
    'Rudra': 9,
    'Veer ': 10,  # Note: There is an extra space at the end of 'Howard'.
}

# Print the original dictionary elements.
print("Original directory elements:")
print(students)

# Call the 'keys_only' function to extract keys and print them as a flat list.
print("\nFlat list of all the keys of the said dictionary:")
print(keys_only(students)) 
