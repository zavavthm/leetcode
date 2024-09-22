from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i = len(nums)-1

        while(nums[i] <= nums[i-1] and i > 0):
            i-=1
        if i == 0:
            nums.sort()
            return
        else:
            # if the code entered else section means it found the transition point
            i = i-1
            print(i)
            # find number greater than nums[i] towards the right side.
            temp = 101 #one more than max possible value for the problems
            temp_index = -1
            for itr in range(len(nums)-1, i, -1):
                if nums[itr] < temp and nums[itr] > nums[i]:
                    temp = nums[itr]
                    temp_index = itr
            
            tmp = nums[i]
            nums[i] = temp
            nums[temp_index] = tmp
            nums[i+1:] = nums[i+1:][::-1]
        print(nums)
            

obj = Solution()
l = [
    [4,8,8,8,9,7,7,6,4,3],
    [2,3,1,3,3],
    [2,2,0,4,3,1],
    [4,2,0,2,3,2,0],
    [2,3,1],
    [1,2,3],
    [3,2,1],
    [2,1,3],
    [1,3,2],
    [],
    [0],

]
for i in l:
    print('I/P:',i)
    obj.nextPermutation(i)
    break