nums = [1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,8,8]

n = len(nums)
freq_map = {}
for i in range(0, n):
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:
    nums[j] = k
    j +=1

print(nums)