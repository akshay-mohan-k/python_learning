nums = [1,1,1,2,2,3,3,3,4,4,4,5,5,6,7,8,8,8]

n = len(nums)
i = 0
j = 1

for j in range(1, n):
    if nums[j] != nums[j-1]:
        i += 1
        nums[i] = nums[j]

print(nums)
