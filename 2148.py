from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        count = 0
        for num in nums:
            if num < max_num and num > min_num:
                count += 1
        return count
    
obj = Solution()
nums = [-3, 3, 3, 9]
print(obj.countElements(nums))