from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = []
        for char in s:
            if char == '#':
                if len(ls) > 0:
                    ls.pop()
            else:
                ls.append(char)
        index = len(ls)
        for char in t:
            if char == '#':
                if len(ls) > index:
                    ls.pop()
            else:
                ls.append(char)
        return ls[:index] == ls[index:]

obj = Solution()
s = "y#fo##f"
t = "y#f#o##f"
print(obj.backspaceCompare(s,t))
