import math

nums = [2, 6, 1, 8, 4, 9, 7]

def second_largest(nums):
    largest = -math.inf
    second_largest = -math.inf
    for i in range(0, len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    return second_largest


print(second_largest(nums))