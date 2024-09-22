from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        f = float('inf')
        s = float('inf')

        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            else:
                return True      
        return False

obj = Solution()
#nums = [5,3,4,3,2,1,0,1,0,3]
# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
nums = [20,100,10,12,5,13]
print(obj.increasingTriplet(nums))