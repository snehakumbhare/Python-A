#Python Bloom Filter implementation
#Write a Python program that implements a Bloom filter for probabilistic data structures.
import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size  # Size of the bit array
        self.hash_count = hash_count  # Number of hash functions
        self.bit_array = [0] * size  # Bit array to store elements

    def _hashes(self, item):
        """Generate hash_count hashes for the item using different hash functions."""
        hashes = []
        for i in range(self.hash_count):
            # Create a unique hash for each iteration
            hash_result = int(hashlib.md5((str(item) + str(i)).encode()).hexdigest(), 16) % self.size
            hashes.append(hash_result)
        return hashes

    def add(self, item):
        """Add an item to the Bloom filter."""
        hashes = self._hashes(item)
        for hash_value in hashes:
            self.bit_array[hash_value] = 1

    def check(self, item):
        """Check if an item is possibly in the Bloom filter."""
        hashes = self._hashes(item)
        return all(self.bit_array[hash_value] == 1 for hash_value in hashes)

# Example usage
size = 1000  # Size of the bit array
hash_count = 10  # Number of hash functions

bloom_filter = BloomFilter(size, hash_count)

# Add items to the Bloom filter
bloom_filter.add("Red")
bloom_filter.add("Green")
bloom_filter.add("Blue")
bloom_filter.add("Orange")

# Check for item membership
print("Red in filter:", bloom_filter.check("Red"))  # Should be True
print("Green in filter:", bloom_filter.check("Green"))  # Should be True
print("Orange in filter:", bloom_filter.check("Orange"))  # Should be True
print("Black in filter:", bloom_filter.check("Black"))  # Should be False (most likely)
