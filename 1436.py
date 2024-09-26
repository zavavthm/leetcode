from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sS, sD = set(), set()
        for source, destination in paths:
            sS.add(source)
            sD.add(destination)
        return (sD - sS).pop()

obj = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(obj.destCity(paths))