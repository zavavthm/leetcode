from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        for i in range(len(words)-1):
            j = 0
            flag = False
            min_ = min(len(words[i]), len(words[i+1]))
            while j < min_ and order.find(words[i][j]) <= order.find(words[i+1][j]):
                if order.find(words[i][j]) < order.find(words[i+1][j]):
                    flag = True
                    break
                j+=1
            if flag:
                continue
            if len(words[i+1]) == min_:
                if len(words[i]) != min_:
                    return False
                else:
                    if words[i+1][-1] != words[i][-1]:
                        return False
            if j < min_:
                return False
                
        return True

obj = Solution()
words = ["hello","hello"]
s = "worldabcefghijkmnpqstuvxyz"
print(obj.isAlienSorted(words, s))