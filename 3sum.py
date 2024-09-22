## Approach 3: my idea

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        freq = {}
        left = []
        right = []
        i = 0

        #removing duplicates and creating a freq hash map
        while i < len(nums):
            if nums[i] in freq:
                freq[nums[i]] += 1
                if nums[i] == 0:
                    if freq[nums[i]] == 3:
                        triplets.append([0,0,0])
                    nums.pop(i)
                else:
                    if freq[nums[i]] >= 2:
                        nums.pop(i)
            else:
                freq[nums[i]] = 1
                i+=1
        
        nums.sort()

        print(nums)

        for i in range(len(nums)-1):
            j = i
            k = len(nums)-1
            if nums[i] > 0:
                break
            # only get sum if j < k AND atleast one number is less than 0 AND atleast one number is greater than 0
            while j <= k and (nums[i] < 0 or nums[j] < 0 or nums[k] < 0) and (nums[i] > 0 or nums[j] > 0 or nums[k] > 0):
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0:
                    if ((i == j and freq[nums[i]] > 1) or (k == j and freq[nums[j]] > 1) or (i == k and freq[nums[i]] > 1)):
                        triplets.append([nums[i], nums[j], nums[k]])
                    elif i != j and j != k and i != k:
                        triplets.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif sum_ < 0:
                    j+=1
                else:
                    k-=1

        return triplets
            

            
if __name__ == "__main__":
    
    l = [
        [-1,0,1],
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
        [1,1,-2],
        [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    ]
# [[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]]
    obj = Solution()
    for i in l:
        print(obj.threeSum(i))
        




## Approach 2: Taken from one of the solutions submitted

# from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         target = 0
#         l = len(nums)
#         nums.sort()
#         triplets = []

#         for i in range(l-2):
#             j = i+1
#             k = l-1
#             if nums[i] == nums[i-1] and i > 0:
#                 continue
#             while j < k:
#                 sum_ijk = nums[i] + nums[j] + nums[k]
#                 if sum_ijk == target:
#                     triplets.append([nums[i], nums[j], nums[k]])
#                     j+=1
#                     k-=1
#                     while j < k and nums[j] == nums[j-1]:
#                         j+=1
#                     while j < k and nums[k] == nums[k+1]:
#                         k-=1
#                 elif sum_ijk < target:
#                     j+=1
#                 else:
#                     k-=1
        
#         return triplets


# if __name__ == "__main__":
    
#     l = [
#         [-1,0,1],
#         [-1,0,1,2,-1,-4],
#         [0,1,1],
#         [0,0,0],
#         [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
#     ]
# # [[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]]
#     obj = Solution()
#     for i in l:
#         print(obj.threeSum(i))
        






## Approach 2: It's inefficient. Takes a lot of time.


# from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         l = len(nums)
#         triplets = []
#         triplet_indices = []
#         nums = sorted(nums)
        
#         def find_cmp(i, j, cmp):
#             for z in range(l):
#                 if cmp == nums[z] and z != i and z != j:
#                     return z
#             return -1

#         def check_no_dup(i, j, k):
#             set_ijk = set([i,j,k])
#             set_nums_ijk = set([nums[i],nums[j],nums[k]])
#             if len(triplet_indices) == 0:
#                 return True
#             for triplet in triplet_indices:
#                 if set_ijk == set(triplet):
#                     return False
#             for triplet in triplets:
#                 if set_nums_ijk == set(triplet):
#                     return False
#             return True

#         for i in range(l-1):
#             for j in range(i+1,l):
#                 cmp = -(nums[i] + nums[j])
#                 if cmp < nums[j]:
#                     continue
#                 cmp_index = find_cmp(i, j, cmp)
#                 if cmp_index == -1 or cmp_index <= j:
#                     continue
#                 if check_no_dup(i, j, cmp_index):
#                     triplets.append([nums[i],nums[j],nums[cmp_index]])
#                     triplet_indices.append([i,j,cmp_index])

#         return triplets

# if __name__ == "__main__":
    
#     l = [
#         [-1,0,1],
#         [-1,0,1,2,-1,-4],
#         [0,1,1],
#         [0,0,0],
#         [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
#     ]

#     obj = Solution()
#     for i in l:
#         print(obj.threeSum(i))
        