class Solution:
    def addStrings(self, n1: str, n2: str) -> str:
        if len(n1) > len(n2):
            n2 = '0'*(len(n1)-len(n2))+n2
        elif len(n2) > len(n1):
            n1 = '0'*(len(n2)-len(n1))+n1
        carry = 0
        sum_str = ''
        for i in range(len(n1)-1,-1,-1):
            sum_ = int(n1[i]) + int(n2[i]) + carry
            remainder = sum_%10
            carry = sum_//10
            sum_str = str(remainder) + sum_str
        if carry != 0:
            sum_str = str(carry) + sum_str
        return sum_str

obj = Solution()
n1 = "2354325"
n2 = "325535"
print(obj.addStrings(n1, n2))