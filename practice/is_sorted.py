nums = [2, 3, 4, 5, 6, 7]

def is_sorted(nums):
    for i in range(0, len(nums)-1):
        if(nums[i] > nums[i+1]):
            return False
    return True

print(is_sorted(nums))