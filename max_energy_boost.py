## Approach 2:

class Solution:
    def maxEnergyBoost(self, A, B):
        pass

obj = Solution()
print(obj.maxEnergyBoost([4,1,1],[1,1,3]))
# print(obj.maxEnergyBoost([1,3,1],[1,1,3]))
# print(obj.maxEnergyBoost([3,3,3],[3,4,6]))
# print(obj.maxEnergyBoost([3,3,4],[4,3,4]))
# print(obj.maxEnergyBoost([5,5,6,3,4,3,3,4],[5,3,3,4,4,6,6,3]))
# print(obj.maxEnergyBoost([4,3,5,3,4,5,6,6,5], [5,5,4,5,6,3,3,4,3]))




# from typing import List

# class Solution:
#     def maxEnergyBoost(self, A, B):
#         i = sum_ = 0
#         itr = True
#         d = {
#             True:A,
#             False:B
#         }
#         l = len(A)
#         if A[i] < B[i]:
#             a = B
#             b = A
#         else:
#             a = A
#             b = B

#         while i < l:
#             if i == l-1:
#                 sum_ += d[itr][i]
#                 break
#             if i < l-1 and d[itr][i] >= d[not itr][i] and d[itr][i] >= d[not itr][i+1]:
#                 # not to switch
#                 sum_ += d[itr][i]
#                 i+=1
#             elif i < l-1 and d[not itr][i+1] >= d[itr][i] and d[not itr][i] >= d[itr][i+1]:
#                 sum_ += d[not itr][i+1]
#                 i+=2
#                 itr = False
#             else:
#                 itr = True
#                 sum_ += d[itr][i]
#                 i+=1
#         sumA = sum(A)
#         sumB = sum(B)
#         print(sum_, sumA, sumB)
#         if sum_ > sumA and sum_ > sumB:
#             return sum_
#         return sumA if sumA > sumB else sumB


# obj = Solution()
# print(obj.maxEnergyBoost([4,1,1],[1,1,3]))
# print(obj.maxEnergyBoost([1,3,1],[1,1,3]))
# print(obj.maxEnergyBoost([3,3,3],[3,4,6]))
# print(obj.maxEnergyBoost([3,3,4],[4,3,4]))
# print(obj.maxEnergyBoost([5,5,6,3,4,3,3,4],[5,3,3,4,4,6,6,3]))
# print(obj.maxEnergyBoost([4,3,5,3,4,5,6,6,5], [5,5,4,5,6,3,3,4,3]))

