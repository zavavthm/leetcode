from typing import List

class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        for i, num in enumerate(nums):
            print(i, num)
        return 0


l = [
    [1,2,3,4,5,6,7]
]
obj = Solution()
for nums in l:
    print(obj.twoSum(nums, 7))



## Approach 2: less faster

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], t: int) -> List[int]:
#         def find_complement(start, end):
#             if start > end:
#                 return -1
#             mid = (start+end)//2
#             if t == nums[mid]:
#                 return mid
#             elif t > nums[mid]:
#                 return find_complement(mid+1, end)
#             else:
#                 return find_complement(start, mid-1)
        
#         hash_map = {}

#         for i in range(len(nums)):
#             if nums[i] in hash_map:
#                 del hash_map, nums
#                 return [hash_map[nums[i]], i]
#             hash_map[t-nums[i]] = i
        
#         return -1


# l = [
#     [1,2,3,4,5,6,7]
# ]
# obj = Solution()
# for nums,target in l:
#     print(obj.twoSum(nums, target))
