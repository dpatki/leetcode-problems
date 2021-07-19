#submitted 11/07/2021
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        prev = [poured]
        current = [0,0]
        for i in range(query_row):
            for j in range(len(prev)):
                current[j] += (max(prev[j] - 1, 0)) / 2
                current[j+1] += ((max(prev[j] - 1, 0))) / 2
            prev = current
            current = [0] * (len(prev) + 1)

        return min(prev[query_glass], 1)
        