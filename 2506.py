from typing import List

# Approach 2: 100% faster
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        hm = {}
        for word in words:
            f_set = set(word)
            hm[f_set] = hm.get(f_set,0) + 1
        
        for value in hm.values():
            count += value*(value-1)//2
        
        return count

# Approach 1: 97% faster
# class Solution:
#     def similarPairs(self, words: List[str]) -> int:
#         count = 0
#         for i in range(len(words)):
#             words[i] = set(words[i])
#         for i in range(len(words)-1):
#             for j in range(i+1, len(words)):
#                 if words[i] == words[j]:
#                     count+=1
#         return count


obj = Solution()
words = ["nba", "cba", ]
print(obj.similarPairs(words))