class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sub = {
            'I': ['X', 'V'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        
        num = i = 0

        while i < len(s):
            if s[i] in sub:
                if i < len(s)-1 and s[i+1] in sub[s[i]]:
                    num += d[s[i+1]] - d[s[i]]
                    i += 2
                    continue
                else:
                    num += d[s[i]]
            else:
                num += d[s[i]]
            i+=1
        return num

if __name__ == "__main__":
    
    roman_nums = [
        "III",
        "XL",
        "XCXLVIII",
        "",
        "M"
    ]

    obj = Solution()
    for num in roman_nums:
        print(obj.romanToInt(num))
        #break