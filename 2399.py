from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ls = []
        for i in range(len(s)):
            if s[i] not in ls:
                index = distance[ord(s[i])-97]+i+1
                if index >= len(s) or s[index] != s[i]:
                    return False
                ls.append(s[i])
        return True

obj = Solution()
s = "zz"
distance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
print(obj.checkDistances(s, distance))