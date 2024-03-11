# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

def contains_duplicate(nums):
    cache = {}
    for i in nums:
        if i not in cache:
            cache[i] = i
        else:
            return True
    return False


print(contains_duplicate([1, 2, 3, 4, 5, 2]))
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 2]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 2, 3, 4, 5]))
