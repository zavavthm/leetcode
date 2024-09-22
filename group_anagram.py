
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ip = {}
        for i in range(len(strs)):
            sorted_chars = "".join(sorted(strs[i]))
            print(sorted_chars)
            if sorted_chars in ip.keys():
                ip[sorted_chars].append(strs[i])
            else:
                ip[sorted_chars] = [strs[i]]
        
        return list(ip.values())



obj = Solution()
l = [
    ['dggggg','dddddg'],
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]

for i in l:
    i.sort()
    print(obj.groupAnagrams(i))


## Approach 1: <Inefficient approach but the most intuitive one>

# from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         # fn to convert string to list ['e','a','t']
#         def str_to_list(string):
#             return [str(char) for char in string]
        
#         def get_freq(itr):
#             freq = {}
#             for char in itr:
#                 if char in freq.keys():
#                     freq[char] += 1
#                 else:
#                     freq[char] = 1
#             return freq

#         def check_anagram(string, list_chars):
#             for char in string:
#                 if char not in list_chars:
#                     return False
#             if len(string) == len(list_chars):
#                 freq_list_chars = get_freq(list_chars)
#                 freq_string = get_freq(string)
#                 for key in freq_string.keys():
#                     if freq_string[key] != freq_list_chars[key]:
#                         return False
#                 return True
#             return False
        
#         if len(strs) == 1:
#             return [strs]
#         lst = [
#             {
#                 "elements": str_to_list(strs[0]),
#                 "anagrams":[],
#             }
#         ]

#         for string in strs:
#             flag = False
#             for hash_table in lst:
#                 if check_anagram(string, hash_table['elements']):
#                     print(string)
#                     flag = True
#                     hash_table['anagrams'].append(string)
#                     break
#             if not flag:
#                 lst.append({"elements": string, "anagrams":[string]})
#         print(lst)
#         return [hash_table['anagrams'] for hash_table in lst]


#         # for str in strs:
#         #     # check if all chars in str exist in list of existing hash tables and len(str) == existing str length
#         #     existing_str[anagram].append(str)
#         #     #else
#         #     insert into the list of hash_tables




# obj = Solution()
# l = [
#     ["eat","tea","tan","ate","nat","bat"],
#     [""],
#     ["a"]
# ]

# for i in l:
#     print('I/P:',i)
#     print(obj.groupAnagrams(i))