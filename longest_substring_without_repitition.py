s = "pwwkew"

def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    l = len(s)
    if l == 1: return 1
    for i in range(l-1):
        count = 0
        j = i
        d = {}
        while j < l:
            if d.get(s[j]) is None:
                d[s[j]] = 1
                count += 1
            else:
                if count > max_length:
                    max_length = count
                break
            j+=1
        if count > max_length: 
            max_length = count
    return max_length

print(lengthOfLongestSubstring(s))