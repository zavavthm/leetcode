# from typing import List
# from math import ceil, floor

# class & fn:

# obj = Solution()
# s = ""
# ls = []
# a = 0
# print(obj.())

# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         if len(nums) < 3:
#             return False

#         f = float('inf')
#         s = float('inf')

#         for num in nums:
#             if num <= f:
#                 f = num
#             elif num <= s:
#                 s = num
#             else:
#                 return True
                
#         return False

# with open('user.out', 'w') as f:
#     for case in map(loads, stdin):
#         f.write(f'{str(Solution().increasingTriplet(case)).lower()}\n')
# exit()