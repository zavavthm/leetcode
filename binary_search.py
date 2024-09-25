def binary_search(left, right, n):
    if left > right:
        return -1
    mid = (left + right)//2
    if n == nums[mid]:
        return mid
    elif n > nums[mid]:
        return binary_search(mid+1, right, n)
    else:
        return binary_search(0, mid, n)

nums = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(nums), 12)




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