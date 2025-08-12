#Implementing a Python decorator for enforcing type checking on function arguments

#Write a Python program that implements a decorator to enforce type checking on the arguments of a function.
import inspect
def enforce_type_checking(func):
    def wrapper(*args, **kwargs):
        # Get the function signature and parameter names
        signature = inspect.signature(func)
        parameters = signature.parameters

        # Iterate over the positional arguments
        for i, arg in enumerate(args):
            param_name = list(parameters.keys())[i]
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be of type '{param_type.__name__}'")

        # Iterate over the keyword arguments
        for param_name, arg in kwargs.items():
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be of type '{param_type.__name__}'")

        # Call the original function
        return func(*args, **kwargs)

    return wrapper

# Example usage
@enforce_type_checking
def multiply_numbers(x: int, y: int) -> int:
    return x * y

# Call the decorated function
result = multiply_numbers(5, 7)  # No type errors, returns 30
print("Result:", result)

result = multiply_numbers("5", 7)  # Type error: 'x' must be of type 'int'


