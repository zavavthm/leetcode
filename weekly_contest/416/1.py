from typing import List
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        message = set(message)
        bannedWords = set(bannedWords)
        count = 0
        for word in message:
            if word in bannedWords:
                count+=1
            if count == 2:
                return True
        return False

obj = Solution()
message = ["hello","programming","fun"]
bannedWords = ["world","programming","leetcode"]
print(obj.reportSpam(message, bannedWords))
