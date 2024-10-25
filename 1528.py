from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ls = [0]*len(s)
        for i in range(len(s)):
            ls[indices[i]] = s[i]
        return ''.join(ls)

obj = Solution()
s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]
print(obj.restoreString(s,indices))