# efficient solution

from typing import List
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Dictionary mapping digits to letters
        mob_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        # If input digits is empty, return an empty list
        if not digits:
            return []
        
        # Create a list of strings where each string contains the letters for the corresponding digit
        letter_lists = [mob_dict[int(digit)] for digit in digits]
        
        print(letter_lists)

        # Compute the Cartesian product of these lists
        p_list = itertools.product(*letter_lists)

        print(p_list)
        
        # Convert tuples to strings
        result = ["".join(combination) for combination in p_list]
        
        return result




# My Approach:

# from typing import List

# class Solution:
#     hash_map = {
#         2: ['a', 'b', 'c'],
#         3: ['d', 'e', 'f'],
#         4: ['g', 'h', 'i'],
#         5: ['j', 'k', 'l'],
#         6: ['m', 'n', 'o'],
#         7: ['p', 'q', 'r', 's'],
#         8: ['t', 'u', 'v'],
#         9: ['w', 'x', 'y', 'z']
#     }

#     def get_combinations(self, cmbs, num):
#         if len(cmbs) == 0:
#             return self.hash_map[num]
        
#         itr = 0
#         new_cmbs = [0]*(len(cmbs)*len(self.hash_map[num]))
        
#         for i in range(len(cmbs)):
#             for chr in self.hash_map[num]:
#                 new_cmbs[itr] = cmbs[i] + chr
#                 itr+=1
#         return new_cmbs


#     def letterCombinations(self, digits: str) -> List[str]:
#         i = 0
#         l = len(digits)
        
#         if l == 0:
#             return []
        
#         while i < l:
#             cmbs = self.get_combinations(cmbs, int(digits[i]))
#             i+=1
        
#         return cmbs

obj = Solution()
n_digits = [
    # "2",
    # "29",
    "374",
    # "33",
    # "",
    # "6679"
]
for digits in n_digits:
    cmbs = obj.letterCombinations(digits)
    print(cmbs, len(cmbs))