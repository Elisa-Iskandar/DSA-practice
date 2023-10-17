#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def contains_duplicate(nums):
    seen = []
    for x in nums:
        if x not in seen:
            seen.append(x)
        else:
            return True
    return False
    
nums = [1,2,2,3,1]
print(contains_duplicate(nums))
