class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s = date.split('-')
        bin_date = ''
        for x in s:
            bin_date += bin(int(x))[2:] + '-'
        return bin_date[:-1]
obj = Solution()
date = '2020-05-12'
print(obj.convertDateToBinary(date))