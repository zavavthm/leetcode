class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or s[0] in '}])':
            return False
        stack = []
        for chr in s:
            if len(stack) == 0 and chr in '}])':
                return False
            if (chr == ')' and stack[-1] == '(') or (chr == ']' and stack[-1] == '[') or (chr == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                stack.append(chr)
        return len(stack) == 0

obj = Solution()
print(obj.isValid("{{{{{{{{}}}}}}}}"))