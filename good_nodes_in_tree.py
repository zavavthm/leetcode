from typing import List

count = 0
d = {}

class Node:
    def __init__(self, value, children = []) -> None:
        self.value = value
        self.children = children
        self.isGood = True
    
    def add_child(self, child):
        self.children.append(child)

def count_good_nodes(parent_obj):
    
    if len(parent_obj.children) == 0:
        return 1
    else:
        if parent_obj.isGood == False:
            return 0
        for child in parent_obj.children:
            if count_good_nodes(d[child]) == 1:
                count += 1
            else:
                pass
    
    ## TODO: IN PROGRESS
            
    return count

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        for edge in edges:
            node, child = edge
            if node not in d:
                d[node] = Node(node, [child])
            else:
                d[node].add_child(child)
            d[child] = Node(child)
        
        return count_good_nodes(d.get(0))

obj = Solution()
edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
print(obj.countGoodNodes(edges))