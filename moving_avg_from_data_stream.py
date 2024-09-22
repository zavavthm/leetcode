class MovingAverage:

    def __init__(self, size: int):
        self.size = size

    def next(self, val: int) -> float:
        pass


# Your MovingAverage object will be instantiated and called as such:
ops = ["MovingAverage","next","next","next","next"]
vals = [[3],[1],[10],[3],[5]]
obj = MovingAverage(vals[0])

for i in range(len(vals)):
    exec(f"param_{i} = obj.next(vals[i])")
    print(f"param_{i}")