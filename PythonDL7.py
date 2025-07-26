#Implement a Decorator to Enforce Rate Limits on a Function

#Write a Python program that implements a decorator to enforce rate limits on a function.
import time

def rate_limits(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()

        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset

            # Calculate time elapsed since last reset
            elapsed = time.time() - last_reset

            # If elapsed time is greater than the period, reset the call count
            if elapsed > period:
                calls = 0
                last_reset = time.time()

            # Check if the call count has reached the maximum limit
            if calls >= max_calls:
                raise Exception("Rate limit exceeded. Please try again later.")

            # Increment the call count
            calls += 1

            # Call the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator

# Maximum 6 API calls are permitted.
@rate_limits(max_calls=6, period=10)
def api_call():
    print("API call executed successfully...")

# Make API calls
for _ in range(8):
    try:
        api_call()
    except Exception as e:
        print(f"Error occurred: {e}")
