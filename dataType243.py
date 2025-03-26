#Python: Geometric progression

#Write a Python program to initialize a list containing the numbers in the specified range where s
#tart and end are inclusive and the ratio between two terms is step. Return an error if step equals 1.

#Use range(), math.log() and math.floor() and a list comprehension to create a list of the appropriate length, applying the step for each element.

#Omit the second argument, start, to use a default value of 1.

#Omit the third argument, step, to use a default value of 2.
# Import the 'floor' and 'log' functions from the 'math' module.
from math import floor, log

# Define a function 'geometric_progression' that calculates a geometric progression.
# It takes the ending value 'end' as a required parameter, and 'start' and 'step' as optional parameters with default values.
def geometric_progression(end, start=1, step=2):
    # Calculate the number of terms in the geometric progression using logarithms and floor division.
    num_terms = floor(log(end / start) / log(step) + 1)
    
    # Use a list comprehension to generate the geometric progression.
    progression = [start * step ** i for i in range(num_terms)]
    
    # Return the list representing the geometric progression.
    return progression

# Call the 'geometric_progression' function with different parameters and print the results.
print(geometric_progression(256))
print(geometric_progression(256, 3))
print(geometric_progression(256, 1, 4)) 
