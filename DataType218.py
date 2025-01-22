#Python: Builds a list, using an iterator function and an initial seed value
#Write a  Python program to build a list, using an iterator function and an initial seed value.

#The iterator function accepts one argument (seed) and must always return a list with two elements ([value, nextSeed]) or False to terminate.
#Use a generator function, fn_generator, that uses a while loop to call the iterator function and yield the value until it returns False.
#Use a list comprehension to return the list that is produced by the generator, using the iterator function.
# Define a function called 'unfold' that generates a list by repeatedly applying a function to a seed value.
def unfold(fn, seed):
  # Define a generator function called 'fn_generator' that will yield values produced by the unfolding process.
  def fn_generator(val):
    while True:
      # Apply the function 'fn' to the second element of 'val' (val[1]).
      val = fn(val[1])
      # If the result is False, stop the unfolding process.
      if val == False:
        break
      # Yield the first element of 'val' (val[0]).
      yield val[0]
  # Create a list by collecting values from the generator using a list comprehension.
  return [i for i in fn_generator([None, seed])]

# Define a lambda function 'f' that produces new values based on the input value.
f = lambda n: False if n > 40 else [-n, n + 10]

# Example usage: Use the 'unfold' function to generate a list of values based on the lambda function 'f' and an initial seed of 10.
print(unfold(f, 10)) 
