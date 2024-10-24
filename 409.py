from collections import Counter
from typing import List
 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        freqs = sorted(hm.values(), reverse = True)
        count = sum([freq if freq&1 == 0 else 0 for freq in freqs])
        
        first_odd = True
        for freq in freqs:
            if freq&1 == 1:
                if first_odd:
                    count += freq
                    first_odd = False
                else:
                    count += freq-1
        return count