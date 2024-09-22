from typing import List

# Efficient Solution
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        prev_occurence = -n

        for i in range(0, n):
            if s[i] == c:
               prev_occurence = i
            ans[i] = i - prev_occurence

        prev_occurence = 2*n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev_occurence = i
            ans[i] = min(ans[i], prev_occurence - i)

        return ans
        

# class Solution:
#     def allOccurences(self, s, c):
#         res = []
#         for i in range(len(s)):
#             if s[i] == c:
#                 res.append(i)
#         return res

#     def shortestToChar(self, s: str, c: str) -> List[int]:
        
#         def getMinDistance(i):
#             return min([abs(index-i) for index in ls])
        
#         ls = self.allOccurences(s, c)
#         res = [0]*len(s)
#         for i in range(len(s)):
#             if s[i] != c:
#                 res[i] = getMinDistance(i)
        
#         return res

obj = Solution()
s = "loveleetcode"
c = "l"
print(obj.shortestToChar(s,c))
