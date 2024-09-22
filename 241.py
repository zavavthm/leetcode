from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for j in left:
                    for k in right:
                        if expression[i] == '+':
                            res.append(j+k)
                        elif expression[i] == '*':
                            res.append(j*k)
                        else:
                            res.append(j-k)
        if len(res) == 0:
            res.append(int(expression))
        return res


obj = Solution()
#exp = "1-2+3*4-5*7+6"
exp = "2-1-1"
print(obj.diffWaysToCompute(exp))
