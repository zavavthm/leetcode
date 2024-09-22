class Solution:
    def numberToWords(self, num: int) -> str:
        hash_map = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Fourty",
            50: "Fixty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        try:
            return hash_map[num]
        except KeyError:
            word = ''
            last_digit = True
            while num > 0:
                if last_digit:
                    digit = num%100
                    ## TODO


obj = Solution()
n_nums = [
    10,
    # "2",
    # "29",
    374,
    # "33",
    # "",
    # "6679"
]
for num in n_nums:
    word = obj.numberToWords(num)
    print(word)

# 0 to 2,147,483,647
