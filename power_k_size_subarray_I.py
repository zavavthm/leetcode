
# Approach 1:
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
#         # pointers i and j iterating thru while loop i and j are starting and end points of the subarray going till the end of the list
#         # EDGE: <if length < k: max_element = -1>
#         # call fn get_max_element (i,j):
#         #   if sorted: 
#         #        return max_element 
#         #   else:
#         #       return -1
#         # appending the num to the list
#         # increment i, j
        def get_max_element(start, end):
            flag = True
            while start < end:
                if nums[start]+1 != nums[start+1]:
                    flag = False
                    break
                start += 1
            if flag:
                return nums[end]
            return -1
        
        i = 0
        j = k-1
        l = len(nums)
        max_arr = [0]*(len(nums)-k+1)
        while j < l:
            max_arr[i] = get_max_element(i,j)
            i+=1
            j+=1
        return max_arr

obj = Solution()
nums = [
    [3,2,3,2,3,2,3],
    [1],
    [2,2,2,2,2],
    [1,7,8]
    ]
k = [2,2,3,2]
for nums, k in zip(nums, k):
    print(obj.resultsArray(nums,k))



