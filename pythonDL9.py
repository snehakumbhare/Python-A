#Implementing a Python decorator for exception handling with a default response
#Write a Python program that implements a decorator to handle exceptions raised by a function and provide a default response.
def handle_exceptions(default_response):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Call the original function
                return func(*args, **kwargs)
            except Exception as e:
                # Handle the exception and provide the default response
                print(f"Exception occurred: {e}")
                return default_response
        return wrapper
    return decorator

# Example usage
@handle_exceptions(default_response="An error occurred!")
def divide_numbers(x, y):
    return x / y

# Call the decorated function
result = divide_numbers(7, 0)  # This will raise a ZeroDivisionError
print("Result:", result)
