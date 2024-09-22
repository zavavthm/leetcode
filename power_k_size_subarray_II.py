# Approach 2: efficient one

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
                return nums[end], True
            return -1, False
        def check_sorted(i,j):
            flag = True
            while(i < j):
                if nums[i]+1 != nums[i+1]:
                    flag = False
                    break
                i+=1
            return flag

        i = 0
        j = k-1
        l = len(nums)
        if k == 1:
            return nums
        max_arr = [0]*(len(nums)-k+1)
        flag = False
        if check_sorted(i,j):
            flag = True
        while j < l:
            if flag and nums[j] == nums[j-1]+1:
                max_arr[i] = nums[j]
            else:
                if nums[j] != nums[j-1]+1:
                    max_arr[i] = -1
                    flag = False
                elif not flag:
                    flag = check_sorted(i,j)
                
            i+=1
            j+=1
        return max_arr

obj = Solution()
nums = [
    [3,2,3,2,3,2,3],
    [1],
    [1,2],
    [1,1],
    [1,1],
    [2,2,2,2,2],
    [1,7,8]
    ]
k = [2,2,2,2,1,3,2]
for nums, k in zip(nums, k):
    print(obj.resultsArray(nums,k))



