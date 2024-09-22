from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        itr = 0
        for cmd in commands:
            if cmd == "LEFT":
                itr-=1
            elif cmd == "RIGHT":
                itr+=1
            elif cmd == "UP":
                itr-=n
            else:
                itr+=n
        return itr

            

obj = Solution()
n = 3
commands = ["DOWN", "RIGHT", "UP"]
print(obj.finalPositionOfSnake(n, commands))