from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        suffix = 1
        ans[0] = 1
        ans[1] = nums[0]

        for i in range(2,len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        print(ans)
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix * nums[i+1]
            ans[i] = ans[i]*suffix
        return ans



obj = Solution()
nums = [
    [1,2,3,4],
    [1,2],
    [1,2,3],
    [0,0,1],
    [1,2,3,4,5,6,7,0],
    [2,3,5,0] # p [1,2,6,]
    ]
for num in nums:
    print(obj.productExceptSelf(num))