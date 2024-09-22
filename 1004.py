from typing import List

## Efficient solution taken from someone:
class Solution:
    def longestOnes(self, A, K):
        begin = 0
        for end in range(len(A)):
            K -= 1 - A[end]
            if K < 0:
                K += 1 - A[begin]
                begin += 1
            print("num: {0} begin: {1} end: {2} k: {3}".format(A[end], begin, end, K))
        return end - begin + 1

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         # algorithm:
#         # set w to len(nums)
#         # set a loop where I'll be iterating 'w' from len(nums) to 1 (min window size)
#         # checking for every sliding window of size w, if count_bits(1s) + k >= w
#         # How? 
#         # for every window size, run the for loop for all windows.
#         # check the count of 1s and compare with prev count_bits(1s) + k
#         # if gt, replace, else continue
#         # at the end, return prev

#         ## Getting Time Limit exceeded 
#         w = len(nums)
#         while w > 0:
#             i = 0
#             window_sum = sum(nums[i:i+w])
#             while i < len(nums)-w+1:
#                 if i > 0:
#                     if nums[i-1] == 1:
#                         window_sum-=1
#                     if nums[i+w-1] == 1:
#                         window_sum+=1
#                 if window_sum + k >= w:
#                     return w
#                 i+=1
#             w-=1
#         return 0

obj = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(obj.longestOnes(nums, k))
