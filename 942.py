from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        d = len(s)
        i = idx = 0
        ls = [0]*(d+1)
        for char in s:
            if char == 'D':
                ls[idx] = d
                d-=1
            else:
                ls[idx] = i
                i+=1
            idx+=1
        ls.append(d)
        return ls

obj = Solution()
s = 'IDIDIDIDIDIDIDIDIDD'
print(obj.diStringMatch(s))