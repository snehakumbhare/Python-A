#Python Exercises: Extract the first n number of vowels from a string

#Write a Python program to extract the first specified number of vowels from a given string. If the specified number is less than the number of vowels present in the string then display "n is less than the number of vowels present in the string".
# Define a function named 'test' that takes two inputs: 'text' (a string) and 'n' (an integer).
def test(text, n):
    # Initialize an empty string 'result_str' to store the vowels from 'text'.
    result_str = ''
    
    # Iterate through each character 'i' in the 'text'.
    for i in text:
        # Check if 'i' is a vowel (either lowercase or uppercase).
        if i in 'aioueAEIOU':
            # If 'i' is a vowel, add it to 'result_str'.
            result_str += i
    
    # Check if the length of 'result_str' is greater than or equal to 'n'.
    # If it is, return the first 'n' vowels from 'result_str'.
    # If not, return a message indicating that 'n' is less than the number of vowels in the string.
    return result_str[:n] if len(result_str) >= n else 'n is less than the number of vowels present in the string.'

# Define the original string 'word' and the number 'n'.
word = "Python"
n = 2
print("Original string and number:", word, ",", n)

# Call the 'test' function to extract the first 'n' vowels from the string 'word'.
print("Extract the first n number of vowels from the said string:")
print(test(word, n))

# Define another string 'word' and a different number 'n'.
word = "Python Exercises"
n = 3
print("\nOriginal string and number:", word, ",", n)

# Call the 'test' function with the new inputs to extract the first 'n' vowels from the string.
print("Extract the first n number of vowels from the said string:")
print(test(word, n))

# Define a string 'word' consisting of only vowels and a different number 'n'.
word = "AEIOU"
n = 3
print("\nOriginal string and number:", word, ",", n)

# Call the 'test' function with the vowel-only string and 'n' to extract the first 'n' vowels.
print("Extract the first n number of vowels from the said string:")
print(test(word, n)) 
