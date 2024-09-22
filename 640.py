from typing import List

class Solution:
    def getXTerm(self, right, i):
        # get the x term out of the right side and return it
        pass

    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        l, r = len(left), len(right)
        x_terms = []
        for i in range(r):
            if right[i] == 'x':
                x_terms.append(self.getXTerm(right, i))

        print(left, right)

obj = Solution()
eqn = "x-2+2x=4x-5+6"
print(obj.solveEquation(eqn))
