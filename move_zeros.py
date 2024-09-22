from typing import List
class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr
    
    def print(self):
        print(self.arr)

    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        itr = 0
        while i < len(arr):
            if arr[i] == 0:
                i+=1
            else:
                arr[itr] = arr[i]
                itr+=1
                i+=1
        while itr < len(arr):
            arr[itr] = 0
            itr+=1

arr = [1,2,3,0,0,2,13]
obj = Solution(arr)
obj.moveZeroes(arr)
obj.print()