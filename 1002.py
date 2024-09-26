from typing import List
from functools import reduce
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return reduce(lambda a,b: a & b, map(Counter, words)).elements()

obj = Solution()
words = ["manik", "madman", "maker", "maniac", "meteorite"]
print(obj.commonChars(words))