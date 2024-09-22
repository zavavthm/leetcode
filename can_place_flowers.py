from typing import List
from math import ceil

# efficient solution 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n-=1
            if n == 0:
                return True
        
        return False


# My approach

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n == 0:
#             return True
#         if len(flowerbed) == 1:
#             if flowerbed[0] == 0:
#                 return True
#             return False
#         new = 0
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 1:
#                 continue
#             if i == 0:
#                 if flowerbed[i+1] == 0:
#                     flowerbed[i] = 1
#                     new+=1
#             elif i == len(flowerbed)-1:
#                 if flowerbed[i-1] == 0:
#                     flowerbed[i] = 1
#                     new+=1
#             elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#                 if flowerbed[i] == 0:
#                     flowerbed[i] = 1
#                     new+=1
#             if new == n:
#                 return True
#         return False

obj = Solution()
nums = [0,0,1,0,0]
n = 1
print(obj.canPlaceFlowers(nums, n))