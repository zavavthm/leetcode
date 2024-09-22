class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        else:
            b = '0'*(len(a)-len(b)) + b
        
        carry = 0
        s = ''

        for i in range(len(a)-1, -1, -1):
            if a[i] == b[i]:
                if carry == 1:
                    if a[i] == '0':
                        carry = 0
                    s = '1' + s
                else:
                    if a[i] == '1':
                        carry = 1
                    s = '0' + s
            else:
                if carry == 1:
                    s = '0' + s
                    carry = 1
                else:
                    s = '1' + s
        if carry == 1:
            return '1' + s
        return s


obj = Solution()
print(obj.addBinary('1010','1011'))