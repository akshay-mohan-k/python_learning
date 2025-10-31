nums = [1, 2, 4, 2, 7, 9, 24]

def largest(nums):
    large = nums[0]
    for i in range(1, len(nums)):
        if(nums[i] > large):
            large = nums[i]
    return large

print(largest(nums))
