# Approach 1:
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # approach:
        # starting from the mth and nth position of both lists, we'll get the greater number and insert it at the end of the num1 list and 
        # follow this approach to the first element of either lists. 

        l = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[l] = nums1[m-1]
                m -= 1
            else:
                nums1[l] = nums2[n-1]
                n -= 1
            l -= 1
    
        for i in range(n, 0, -1):
            nums1[l] = nums2[i-1]
            l -= 1
    
obj = Solution()
nums1 = [1,1,1,0,0,0]
nums2 = [0,0,0]
obj.merge(nums1, 3, nums2, 3)
print(nums1)