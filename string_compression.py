# Leetcode Problem No: 443
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        # Algorithm: 3 pointer problem
        # ptr1 - points to the 0th index in the begining, keeping track of index where to update the char and its freq
        # ptr2 - point to first occurence of character to be compared
        # ptr3 - count the freq of the char
        # 1 -> 0, 2 -> 0, 3 -> 1
        # In a while loop, till chars[ptr3] == chars[ptr2]: ptr3+=1
        # outide of loop, ptr3 will point to the next char, so freq = ptr3-ptr2
        # since ptr3 will point to the next char, so ptr2 = ptr3
        # and ptr3+=1
        #
        # Updating ptr1 with char & its freq
        # chars[ptr1] = char
        # ptr1+=1
        # if freq == 1:
        # continue
        # elif freq < 10:
        #     chars[ptr1] = str(freq)
        #     ptr1+=1  
        # else:
        #     freq = str(freq)
        #     ## -- add each char to the ptr1 and increment it by 1
        # return ptr1
        ptr1, ptr2, ptr3 = 0, 0, 1
        while ptr3 < len(chars):
            while ptr3 < len(chars) and chars[ptr2] == chars[ptr3]:
                ptr3+=1
            freq = ptr3-ptr2
            chars[ptr1] = chars[ptr2]
            ptr1+=1
            if freq > 9:
                for dgt in str(freq):
                    chars[ptr1] = dgt
                    ptr1+=1
            elif freq > 1:
                chars[ptr1] = str(freq)
                ptr1+=1
            ptr2 = ptr3
            ptr3+=1
            if ptr2 == len(chars)-1:
                chars[ptr1] = chars[ptr2]
                return ptr1+1
        return ptr1 if len(chars) > 1 else 1
        


obj = Solution()
#s = ["a","b","c"]
#s = ["a","a","b","b","c","c","c"]
#s = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
s = ['a',"b","b","b","b","b","b","b","b","b","b","b","c","d"]
print(s[:obj.compress(s)])



# from typing import List
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         if len(chars) == 1:
#             return 1
        
#         def insert_num(ptr, num):
#             chars[ptr] = chars[ptr]
#             for char in str(num):
#                 chars[ptr] = char
#                 ptr+=1
#             return ptr
        
#         ptr1, ptr2, ptr3 = 0, 1, 0
#         while ptr2 < len(chars):
#             while ptr2 < len(chars) and chars[ptr1] == chars[ptr2]:
#                 ptr2+=1
#             if ptr2 == ptr1+1:
#                 ptr1+=1
#                 ptr2+=1
#                 ptr3+=1
#             else:
#                 chars[ptr3] = chars[ptr1]
#                 ptr3 = insert_num(ptr3+1, ptr2-ptr1)
#                 ptr1 = ptr2
#                 ptr2+=1
#         print(ptr1, ptr2, ptr3)
#         return chars

# obj = Solution()
# s = 'a a b b c c c'
# print(obj.compress(s.split()))