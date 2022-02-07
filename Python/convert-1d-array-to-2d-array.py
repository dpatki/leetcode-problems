#submitted 13/01/2022
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n*m:
            return []
        output = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[i*n+j])
            output.append(temp)
        return output