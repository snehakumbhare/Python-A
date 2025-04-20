#Python: Generate a list, containing the Fibonacci sequence, up until the nth term
#Write a Python program to generate a list containing the Fibonacci sequence, up until the nth term.

#Starting with 0 and 1, use list.append() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reaches n.
#If n is less or equal to 0, return a list containing 0.
 # Define a function named 'fibonacci_nums' that generates a list of Fibonacci numbers up to the nth value.
def fibonacci_nums(n):
    # Check if n is non-positive (less than or equal to 0).
    if n <= 0:
        # Return a list containing only 0 when n is not positive.
        return [0]
    	
    # Initialize the Fibonacci sequence with the first two values, 0 and 1.
    sequence = [0, 1]
    
    # Continue generating the sequence until it reaches the desired length (n).
    while len(sequence) <= n:
        # Calculate the next value by adding the last two values in the sequence.
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        # Append the next value to the sequence.
        sequence.append(next_value)
    
    # Return the list of Fibonacci numbers.
    return sequence

# Print the first 7 Fibonacci numbers.
print("First 7 Fibonacci numbers:")
print(fibonacci_nums(7))

# Print the first 15 Fibonacci numbers.
print("\nFirst 15 Fibonacci numbers:")
print(fibonacci_nums(15))

# Print the first 50 Fibonacci numbers (for demonstration purposes).
print("\nFirst 50 Fibonacci numbers:")
print(fibonacci_nums(50)) 
