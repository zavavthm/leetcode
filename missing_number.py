from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        total = (len(nums)*(len(nums)+1))/2
        return int(total - sum_nums)

obj = Solution()
nums_list = [
    [0,2,3,4],
    [1],
    [9,6,4,2,3,5,7,0,1]
    ]
for nums in nums_list:
    print(obj.missingNumber(nums))