from typing import List, Optional

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Pointers:
        # if len is not equal, then False
        # more than 2 chars differ from each other False
        # Approach: iterate through them together and count the number of chars which don't match each other. 
        # if != 2: False <If strings are identical, that case will be taken care of here>
        # store the indexes. If s[first] == goal[second] && s[second] == goal[first]:
        # return True
        # else return False
        diff = []
        count = 0
        if len(s) == len(goal) and len(s) >= 2:
            for i in range(len(s)):
                if s[i] != goal[i]:
                    count += 1
                    diff.append(i)
                if count > 2:
                    return False
            if len(diff) == 2:
                return s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
            if count == 0:
                return len(s) > len(set(s))
        return False


obj = Solution()
s = "aaab"
goal = "aaab"
print(obj.buddyStrings(s, goal))
