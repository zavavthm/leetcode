class Solution:
    def myAtoi(self, s: str) -> int:
        
        def removeLeadingCharacters(s, char):
            i = 0
            while i < len(s) and s[i] == char:
                i+=1
            return s[i:]
        
        if len(s) == 0: return 0
        
        flag = False
        
        # remove whitespaces (if any)
        s = removeLeadingCharacters(s, ' ')
        if len(s) == 0:
            return 0
        
        # check and remove +/- sign (if any)
        if s[0] == '-':
            flag = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # remove leading 0s (if any)
        s = removeLeadingCharacters(s, '0')
        if len(s) == 0:
            return 0
        
        if ord(s[0]) < 48 or ord(s[0]) > 57:
            return 0
        
        # read the number
        i = 0
        integer = 0
        while i < len(s) and ord(s[i]) >= 48 and ord(s[i]) <= 57:
            integer = integer*10 + int(s[i])
            i+=1
        min_int = -pow(2, 31)
        max_int = pow(2, 31) - 1
        if flag:
            integer = 0-integer
            
        if integer > max_int:
            return max_int
        elif integer < min_int: 
            return min_int
        return integer

s = "   "

solutionObj = Solution()

print(solutionObj.myAtoi(s))