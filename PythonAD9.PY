#Python LRU Cache Implementation

#Write a Python program to create a caching system with support for LRU eviction policy.

from collections import OrderedDict

# Define a class for the caching system with LRU eviction policy
class LRUCache:
    # Initialize the cache with a maximum capacity
    def __init__(self, capacity):
        self.capacity = capacity  # Set the maximum capacity
        self.cache = OrderedDict()  # Use OrderedDict for O(1) access and ordering

    # Get the value associated with the key from the cache
    def get(self, key):
        # If the key is not in the cache, return -1
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to indicate recent use
        self.cache.move_to_end(key)
        # Return the value associated with the key
        return self.cache[key]

    # Put a key-value pair into the cache
    def put(self, key, value):
        # If the key is already in the cache, update its value and move it to the end
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # If the cache is at capacity, remove the least recently used item
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)  # Remove the first item (least recently used)
            # Add the new key-value pair to the cache
            self.cache[key] = value

# Example usage
if __name__ == "__main__":
    # Create a cache with a capacity of 2
    cache = LRUCache(2)
    # Put key-value pairs into the cache
    cache.put(1, 1)
    cache.put(2, 2)
    # Retrieve and print the value associated with key 1 (should be 1)
    print(cache.get(1))
    # Put a new key-value pair into the cache (evicting key 2)
    cache.put(3, 3)
    # Retrieve and print the value associated with key 2 (should be -1, as it was evicted)
    print(cache.get(2))
    # Retrieve and print the value associated with key 3 (should be 3)
    print(cache.get(3))


