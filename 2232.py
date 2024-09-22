from typing import List

class Solution:
    def minimizeResult(self, expression: str) -> str:
        min_, min_expr = float("inf"), ''
        plus_index = expression.find('+')
        for i in range(plus_index):
            for j in range(plus_index+1,len(expression)):
                if i == 0:
                    expr = '(' + expression[:plus_index] + '+'
                else:
                    expr = expression[:i] + '*(' + expression[i:plus_index] + '+'
                if j == plus_index+1:
                    expr += expression[plus_index+1:] + ')'
                else:
                    expr += expression[plus_index+1:j] + ')*' + expression[j:]
                res = eval(expr)
                if res < min_:
                    min_, min_expr = res, expr
        
        return min_expr.replace('*','')

## another efficient solution
# 
# class Solution:
#     def minimizeResult(self, expression: str) -> str:
#         num1, num2 = expression.split('+')
#         n1, n2 = len(num1), len(num2)
#         min_val = float('inf')
#         result = ""

#         for i in range(n1):
#             for j in range(1, n2 + 1):
#                 print(num1[:i])
#                 left_num = int(num1[:i] or "1")
#                 mid_num = int(num1[i:]) + int(num2[:j])
#                 right_num = int(num2[j:] or "1")
#                 val = left_num * mid_num * right_num
#                 if val < min_val:
#                     min_val = val
#                     result = f"{num1[:i]}({num1[i:]}+{num2[:j]}){num2[j:]}"

#         return result if result else expression

obj = Solution()
expr = "247+3856"
print(obj.minimizeResult(expr))
