from typing import List

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pass

obj = Solution()

wordsDict = ["practice", "makes", "perfect", "coding", "makes", "a", "a"]
word1 = "makes"
word2 = "makes"

print(obj.shortestWordDistance(wordsDict, word1, word2))

# inefficient solution
# from typing import List

# class Solution:
#     def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
#         hm = {
#             word1: [],
#             word2: []
#         }
#         min_dist = pow(10,5)+1
#         for i in range(len(wordsDict)):
#             if word1 == wordsDict[i]:
#                 hm[word1].append(i)
#             if word2 == wordsDict[i]:
#                 hm[word2].append(i)
#         for i in hm[word1]:
#             for j in hm[word2]:
#                 if i != j:
#                     min_dist = min(abs(j-i), min_dist)
            
#         return min_dist

# obj = Solution()

# wordsDict = ["practice", "makes", "perfect", "coding", "makes", "a", "a"]
# word1 = "makes"
# word2 = "practice"

# print(obj.shortestWordDistance(wordsDict, word1, word2))