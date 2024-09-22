from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height)-1
        
        while left < right:

            min_height = height[left] if height[left] < height[right] else height[right]

            area = (right-left)*min_height
            max_area = area if area > max_area else max_area

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return max_area

obj = Solution()
heights = [1,2,4,34,35,46,43,55,34,63,45,24,3,54,745,65,342,22,4,32]
print(obj.maxArea(heights))