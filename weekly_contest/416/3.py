from typing import List
from collections import Counter
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        w1 = Counter(word1)
        w2 = Counter(word2)

        for char in w2:
            if w1[char] < w2[char]:
                return False

obj = Solution()
word1 = "abcabc"
word2 = "aaabc"
print(obj.validSubstringCount(word1, word2))
