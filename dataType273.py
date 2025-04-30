#Python Exercises: Count lowercase letters in a list of words
#Write a Python program to count the lowercase letters in a given list of words.
# Define a function named 'test' that takes a list of words 'text' as input.
def test(text):
    # Use a list comprehension to count the lowercase letters in each word.
    # Iterate through the words in 'text' (outer loop).
    # Iterate through the characters in each word (inner loop).
    # Count the lowercase characters by checking if each character is lowercase.
    # Sum the count of lowercase characters for all words.
    return sum([el.islower() for word in text for el in word])

# Define a list of words 'text'.
text = ["Red", "Green", "Blue", "White"]
print("Original list of words:", text)
# Call the 'test' function to count the lowercase letters in the list of words.
print("Count the lowercase letters in the said list of words:")
print(test(text))

# Define another list of words 'text'.
text = ["SQL", "C++", "C"]
print("\nOriginal list of words:", text)
# Call the 'test' function for the second list of words.
print("Count the lowercase letters in the said list of words:")
print(test(text)) 

