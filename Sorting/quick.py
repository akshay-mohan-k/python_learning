# pick a pivot element and put it in correct position

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        pIndx = partition(nums, low, high)
        quick_sort(nums, low, pIndx - 1)
        quick_sort(nums, pIndx + 1, high)

nums = [8, 3, 6, 4, 10, 2]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
