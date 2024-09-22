from typing import List

class Solution:
    def countBinarySubstrings(self, s):
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        print(s)
        return sum(min(a, b) for a, b in zip(s, s[1:]))


obj = Solution()
s = "11001"
print(obj.countBinarySubstrings(s))
