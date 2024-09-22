# using python inbuilt string manipulation functions:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = s.strip().lower()
        new_str = ''.join(chr for chr in new_str if chr.isalnum())

        l = len(new_str)
        for i in range(l//2):
            if new_str[i] != new_str[l-i-1]:
                return False
        return True

obj = Solution()
s = ""
print(obj.isPalindrome(s))


# Brute Force Approach:
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_str = ''
#         for chr in s:
#             ascii_num = ord(chr)
#             if ascii_num >= 65 and ascii_num <= 90:
#                 new_str += chr.lower()
#             elif (ascii_num >= 97 and ascii_num <= 122) or (ascii_num >= 48 and ascii_num <= 57):
#                 new_str += chr
        
#         l = len(new_str)
#         for i in range(l//2):
#             if new_str[i] != new_str[l-i-1]:
#                 return False
#         return True

# obj = Solution()
# s = ""
# print(obj.isPalindrome(s))