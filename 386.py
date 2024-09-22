from typing import List
from functools import cmp_to_key

class Solution:
    def compare(self, a, b):
        a, b = str(a), str(b)
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
        
    def lexicalOrder(self, n: int) -> List[int]:
        ls = [i for i in range(1,n+1)]
        return sorted(ls, key=cmp_to_key(self.compare))

obj = Solution()
n = 13
print(obj.lexicalOrder(n))