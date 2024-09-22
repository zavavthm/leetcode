class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = l = num = 0
        la, lw = len(abbr), len(word)
        while i < la:
            if abbr[i].isalpha():
                if l < lw and abbr[i] != word[l]:
                    return False
                l+=1
                i+=1
                continue
            while i < la and abbr[i].isdigit():
                if abbr[i] == '0' and num == 0:
                    return False
                num = num*10 + int(abbr[i])
                i+=1
            l+=num
            num=0
        return len("".join(word.split())) == l



obj = Solution()
word = "substitution" # hi
abbr = "su3i1u2on" # 2i
print(obj.validWordAbbreviation(word, abbr))