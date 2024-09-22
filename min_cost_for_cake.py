from typing import List

def minimumCost(m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        cost = hc = vc = 0
        cost_list = [(0, x) for x in horizontalCut] + [(1, x) for x in verticalCut]
        sorted_cost_list = sorted(cost_list, key = lambda x:x[1])

        len_ = len(horizontalCut) + len(verticalCut)

        for i in range(len_-1, -1, -1):
            print(i)
            if sorted_cost_list[i][0] == 1:
                cost += sorted_cost_list[i][1]*(hc+1)
                vc += 1
                print( "for vc: ", cost, hc)
            else:
                cost += sorted_cost_list[i][1]*(vc+1)
                hc += 1
                print( "for hc: ", cost, hc)
        print(hc, vc)
        return cost


if __name__ == "__main__":
    m = 1
    n = 2
    horizontalCut = []
    verticalCut = [4]
    print(minimumCost(m, n, horizontalCut, verticalCut))

