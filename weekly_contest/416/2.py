from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workerTimes = sorted(workerTimes)
        secs, m = 0, 1
        height = 0
        for i in range(len(workerTimes)):
            if height < mountainHeight:
                secs += workerTimes[i]*m
                height += m
        return secs

obj = Solution()
m = 4
w = [2,1,1]
print(obj.minNumberOfSeconds(m,w))