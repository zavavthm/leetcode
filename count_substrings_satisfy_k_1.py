
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        subcount = 0
        for i in range(len(s)):
            count0 = count1 = 0
            for j in range(i, len(s)):
                if s[j] == '0':
                    count0 += 1
                else:
                    count1 += 1
                if count0 <= k or count1 <= k:
                    subcount += 1
        return subcount

obj = Solution()
s = "10101"
k = 1
print(obj.countKConstraintSubstrings(s, k))
