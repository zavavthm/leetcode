class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t)) > 1:
            return False
        n = min(len(s), len(t))
        for i in range(n):
            if s[i] != t[i]:
                if len(s) < len(t):
                    return s[i:] == t[i+1:]
                elif len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                return s[i+1:] == t[i:]
        
        return len(s) != len(t)


# Inefficient solution
# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         if len(t) > len(s):
#             return self.isOneEditDistance(t, s)
#         if len(s)-len(t) > 1:
#             return False
#         if len(s) == len(t):
#             if len(s) == 0:
#                 return False
#             flag = False
#             for i in range(len(s)):
#                 if s[i] != t[i]:
#                     if flag:
#                         return False
#                     flag = True
#             return flag
#         else:
#             for i in range(len(t)):
#                 if s[i] != t[i]:
#                     j = i
#                     while s[j+1] == t[j] and j < len(t)-1:
#                         j+=1
#                     if j < len(t) and s[j+1] != t[j]:
#                         return False
#             return True

                
        

# bleacher
# teacher


obj = Solution()
ls = ['abc', 'abc', 'ad', '', 'ac', 'abc', '11111', 'teacher', 'ab', 'abcd']
lt = ['ad', 'abc', 'awq', '', 'ca', 'ab', '11120', 'bleacher', 'acb', 'bbd']
for s,t in zip(ls, lt):
    print(obj.isOneEditDistance(s, t))