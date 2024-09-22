class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add_strings(a, b):
            pre_zeros = ''
            for _ in range(len(a) - len(b)):
                pre_zeros += '0'
            b = pre_zeros + b
            summ = ''
            carry = 0
            for i in range(len(a)-1, -1, -1):
                tmp_sum = int(a[i]) + int(b[i]) + carry
                remainder = tmp_sum%10
                summ = str(remainder) + summ
                carry = tmp_sum//10
            if carry > 0:
                return str(carry) + summ
            return summ

        def multiply_strings(num1, num2):
            partial_product = []

            if num1 == '0' or num2 == '0':
                return '0'

            for i in range(len(num2)-1,-1,-1):
                partial_product_j = ''
                for _ in range(len(num2)-1-i):
                    partial_product_j += '0'
                carry = 0
                for j in range(len(num1)-1,-1,-1):
                    product = int(num1[j])*int(num2[i]) + carry
                    remainder = product%10
                    partial_product_j = str(remainder) + partial_product_j
                    carry = product//10
                if carry > 0:
                    partial_product_j = str(carry) + partial_product_j
                partial_product.append(partial_product_j)
            
            if len(partial_product) == 1:
                return partial_product[0]

            summ = partial_product[0]
            for i in range(1, len(partial_product)):
                if len(summ) > len(partial_product[i]):
                    summ = add_strings(summ, partial_product[i])
                else:
                    summ = add_strings(partial_product[i], summ)
            
            return summ


        if len(num1) > len(num2):
            return multiply_strings(num1, num2)
        return multiply_strings(num2, num1)


obj = Solution()
num1 = "13"
num2 = "49"
print('I/P:',num1, num2)
print(obj.multiply(num1, num2))