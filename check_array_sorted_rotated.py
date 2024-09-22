from typing import List

# efficient solution
# to count the number of transition points
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count+=1
        if nums[i] > nums[0]:
            count+=1
        return count<=1



# my approach: 
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#         first = nums[0]
#         i = 0
#         while i < len(nums)-1 and nums[i] <= nums[i+1]:
#             i+=1
#         if i == len(nums)-1:
#             return True
#         i+=1
#         while i < len(nums)-1 and nums[i] <= first and nums[i] <= nums[i+1]:
#             i+=1
#         if i == len(nums)-1 and nums[i] <= first:
#             return True
#         return False
        

            
if __name__ == "__main__":
    
    l = [
        [3,1,2,2,4],
        [8,5,4,5,1,4,5,2,2],
        [0,1],
        [1,0],
        [1,2,3,4,5],
        [0,0,0],
        [3,4,5,1,2],
        [2,1,3,4],
        [1,1,1,2,1,1]
    ]
    obj = Solution()
    for i in l:
        print(obj.check(i))