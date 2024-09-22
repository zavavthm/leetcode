from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for i in arr:
            hm[i] = hm.get(i, 0) + 1
        return len(hm) == len(set(hm.values()))

obj = Solution()
arr = [1,2,3,3,3,432,32,52,423,432,432,2,423,432,423,423,4234,234,423]
print(obj.uniqueOccurrences(arr))