from typing import List

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        while s:
            if len(s) >= k:
                if len(s) >= 2*k:
                    res += s[:k][::-1]+s[k:2*k]
                    s = s[2*k:]
                else:
                    res += s[:k][::-1]+s[k:]
                    s=''
            else:
                res += s[::-1]
                s=''
        return res

obj = Solution()
s = "abababababababababa"
k = 2
print(obj.reverseStr(s,k))
