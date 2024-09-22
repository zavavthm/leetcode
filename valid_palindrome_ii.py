from math import ceil
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                w_left = s[left:right]
                w_right = s[left+1:right+1]
                return (w_left == w_left[::-1]) or (w_right == w_right[::-1])
            left+=1
            right-=1
        return True



"""
using mid point and going till that point. It can be further optimized by using left and right pointer as done above.
"""
# from math import ceil
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         l = len(s)
#         m = ceil(l/2)
#         for i in range(m):
#             if s[i]!= s[l-i-1]:
#                 w_left = s[i:l-i-1]
#                 w_right = s[i+1:l-i]
#                 return (w_left == w_left[::-1]) or (w_right == w_right[::-1])
#         return True



"""
solution using recursion --> Dynamic Programming
"""

# from math import ceil
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         return self.isValidPalindrome(s)
    
#     def isValidPalindrome(self, s: str, flag = False) -> bool:
#         l = len(s)
#         if l < 2:
#             return True
#         if l == 3:
#             if s[0] != s[2]:
#                 if flag or (s[1] != s[2] and s[0] != s[1]):
#                     return False
#             return True
#         m = ceil(l/2)
#         for i in range(m):
#             if s[i] != s[l-i-1]:
#                 if flag:
#                     return False
#                 return self.isValidPalindrome(s[i+1:l-i], True) or self.isValidPalindrome(s[i:l-i-1], True)
        
#         return True
        

obj = Solution()
s = [
    "a",
    "aba",
    "abca",
    "abc",
    "atbbga",
    "eedede"
]
for str in s:
    print(obj.validPalindrome(str))