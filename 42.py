from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1. left, right pointing to 2 ends of the list
        2. mid pointing to the 2nd element from left
        3. while left < right, we'll move as per: if left < right: left+=1 else right-=1
        4. if valley created: mid < left & right. Then calculate total
        """

obj = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(obj.trap(heights))