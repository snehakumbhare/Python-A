#Implementing a Python decorator to measure memory usage of a function
#Write a Python program that implements a decorator to measure the memory usage of a function.
import tracemalloc

def measure_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        # Call the original function
        result = func(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        # Print the top memory-consuming lines
        print(f"Memory usage of {func.__name__}:")
        for stat in top_stats[:5]:
            print(stat)

        # Return the result
        return result

    return wrapper

# Example usage
@measure_memory_usage
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Call the decorated function
result = calculate_factorial(5)
print("Factorial:", result)
