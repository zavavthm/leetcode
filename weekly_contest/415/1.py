from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=set()
        ls = []
        count = 0
        for num in nums:
            if num in a:
                ls.append(num)
                count+=1
                if count == 2:
                    break
            else:
                a.add(num)
        return ls

obj = Solution()
nums = [2,3,4,5,7,3,4,2,8]
print(obj.getSneakyNumbers(nums))