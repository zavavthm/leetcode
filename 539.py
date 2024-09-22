from typing import List

## Efficient One: (just convert hours into minues and subtract)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_diff = 1440
        for i in range(len(timePoints)):
            temp = [int(x) for x in timePoints[i].split(":")]
            timePoints[i] = temp[0]*60 + temp[1]
        
        timePoints.sort()

        for i in range(1, len(timePoints)):
            diff = abs(timePoints[i] - timePoints[i-1])
            diff = diff if diff < 720 else 1440 - diff
            min_diff = diff if diff < min_diff else min_diff
        min_diff = min(min_diff, 24*60 - timePoints[-1] + timePoints[0])

        return min_diff

## Inefficient approach
# class Solution:
#     def getTimeDiff(self, a, b):
#         diff = 0
#         a, b = a.split(':'), b.split(':')
#         a, b = [int(x) for x in a], [int(x) for x in b]
#         if a[0] < b[0]:
#             a,b = b,a
#         if a[1] < b[1]:
#             diff += 60+a[1]-b[1]
#             if a[0] == 0:
#                 a[0] = 23
#             else:
#                 a[0]-=1
#         else:
#             diff += a[1]-b[1]
#         diff+= (a[0]-b[0])*60
#         diff = diff if diff < 720 else 1440-diff
#         return abs(diff)

#     def findMinDifference(self, timePoints: List[str]) -> int:
#         min_diff = 1440
#         for i in range(len(timePoints)):
#             for j in range(i+1, len(timePoints)):
#                 if timePoints[i] == timePoints[j]:
#                     return 0
#                 else:
#                     diff = self.getTimeDiff(timePoints[i], timePoints[j])
#                     if diff < min_diff:
#                         min_diff = diff
#         return min_diff

obj = Solution()
ls1 = ["23:59","00:00"]
ls2 = ["00:00","23:59","00:00"]
ls3 = ["01:01","02:01","03:00"]
ls4 = ["01:01","02:01","03:00","03:01"]
print(obj.findMinDifference(ls1))
print(obj.findMinDifference(ls2))
print(obj.findMinDifference(ls3))
print(obj.findMinDifference(ls4))