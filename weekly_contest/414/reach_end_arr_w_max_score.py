from typing import List

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = len(nums)
        i = score = 0
        while i < l-1:
            j = i+1
            while j < l and nums[j] < nums[i]:
                j+=1
            if j == l:
                return score + (j-1-i)*nums[i]
            score += (j-i)*nums[i]
            i=j

        return score


obj = Solution()
nums = [4,1,5]
print(obj.findMaximumScore(nums))