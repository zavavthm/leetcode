from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Approach 3:
        
        """
        count = Counter(nums)
        pairs = 0
        for key, value in count.items():
            if k-key in count:
                if value < count[k-key]:
                    pairs += value
                else:
                    pairs += count[k-key]
        return pairs//2

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         """
#         Efficient Approach 2:
#         """
#         l = len(nums)
#         if l == 1:
#             return 0
#         nums = sorted(nums)
#         i = 0
#         while i < l and nums[i] <= k:
#             i+=1
#         count, left = 0, 0
#         right = i if i < l else l-1
#         while left < right:
#             sum_ = nums[left] + nums[right]
#             if sum_ == k:
#                 count+=1
#                 left+=1
#                 right-=1
#             elif sum_ < k:
#                 left+=1
#             else:
#                 right-=1
#         return count


# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         """
#         Efficient Approach:
#         1. Sort the elements
#         2. Using binary search find element closest to or equal to k
#         3. set left and right pointer to number and the number on the right
#         4. If l+r > k: left-=1, if l+r < k: r-=1 until r >= k
#         5. if l+r == k: count+=1, left+=1, right-=1
#         6. go till the end of the list of r >= k
#         7. return count
#         """
#         l = len(nums)
#         if l == 1:
#             return 0
#         nums = sorted(nums)
#         count, left, right = 0, 0, l-1
#         while left < right:
#             sum_ = nums[left] + nums[right]
#             if sum_ == k:
#                 count+=1
#                 left+=1
#                 right-=1
#             elif sum_ < k:
#                 left+=1
#             else:
#                 right-=1
#         return count


# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         """
#         Inefficient Approach:
#         for every elememt, find the complementary pair for it.
#         If found, make it 0 and count +=1
#         return count
#         """
#         if len(nums) == 1:
#             return 0
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] > 0 and nums[i] < k:
#                 try:
#                     index = nums[i+1:].index(k-nums[i])+i+1
#                 except ValueError:
#                     continue
#                 nums[i] = 0
#                 nums[index] = 0
#                 count+=1
#         return count

obj = Solution()
nums = [2,2,2,3,1,1,4,1]
k = 4
print(obj.maxOperations(nums, k))