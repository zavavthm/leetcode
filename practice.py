# # a = "manik"
# # print("".join(sorted(a)))

# ## Binary search 
# # def binary_search(l, num, start, end):
# #     if start > end:
# #         return -1
# #     mid = (start+end)//2
# #     if num == l[mid]:
# #         return mid
# #     elif num < l[mid]:
# #         return binary_search(l, num, start, mid-1)
# #     else:
# #         return binary_search(l, num, mid+1, end)



# # l = [1,4,5,7,8,20,56,346]

# # index = binary_search(l, 32, 0, len(l)-1)
# # print(index)

# def fn(a,b,*elements):
#     print(type(elements))
#     return a+b
# print(fn(1,2,[1,2,3,4,5]))
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# master_ls = []
# for i in range(len(matrix[0])):
#     ls = []
#     for rows in matrix:
#         ls.append(rows[i])
#     master_ls.append(ls)

# print(master_ls)

# print([[row[i] for row in matrix] for i in range(len(matrix[0]))])

# master_ls = [[rows[i] for rows in matrix] for i in range(len(matrix[0]))]
# print(master_ls)

# def example_function(pos1, pos2, *args, kw1=None, kw2=None, **kwargs):
#     print(f"Positional 1: {pos1}")
#     print(f"Positional 2: {pos2}")
#     print(f"*args: {args}")
#     print(f"Keyword 1: {kw1}")
#     print(f"Keyword 2: {kw2}")
#     print(f"**kwargs: {kwargs}")

# example_function(1, 2, 3, 4, 5, kw1="A", kw2="B", extra="extra value")

import timeit

nums = list(range(10000000))

def fn(num):
    return str(num*num+num/2) + str((num-102452)*12)

def map_approach():
    return list(map(fn, nums))

def comprehension_approach():
    return [str(num*num+num) + str((num-102452)*12) for num in nums]

map_time = timeit.timeit(map_approach, number=10)
comprehension_time = timeit.timeit(comprehension_approach, number=10)

print("Map time:", map_time)
print("Comprehension time:", comprehension_time)

ls = [1,2,3,4,5]