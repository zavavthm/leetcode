def binary_search(nums, k):
    l = len(nums)
    if k == nums[l//2]:
        return l//2
    elif k > nums[l//2]:
        return binary_search(nums[l//2:], k) + l//2
    else:
        return binary_search(nums[:l//2], k)

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k = 65
print(binary_search(nums, k))