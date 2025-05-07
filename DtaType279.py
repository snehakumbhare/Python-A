#Python Exercises: Find all pairs of that differ by three in a list

#Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. 
#Return all pairs of integers in a list.
def test(nums):
    result = []
    for i, x in enumerate(sorted(nums)):
        for y in nums[i+1:]:
            if y == x + 3:
                result.append([x,y])
    return result

nums = [0, 3, 4, 7, 9]
print("Original list:")
print(nums)
print("Find all pairs of that differ by three in the said list:")
print(test(nums))
nums = [0, -3, -5, -7, -8]
print("\nOriginal list:")
print(nums)
print("Find all pairs of that differ by three in the said list:")
print(test(nums))
nums = [1, 2, 3, 4, 5]
print("\nOriginal list:")
print(nums)
print("Find all pairs of that differ by three in the said list:")
print(test(nums))
nums = [100, 102, 103, 114, 115]
print("\nOriginal list:")
print(nums)
print("Find all pairs of that differ by three in the said list:")
print(test(nums))  
