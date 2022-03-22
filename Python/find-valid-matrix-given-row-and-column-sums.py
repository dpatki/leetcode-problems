#submitted 15/03/2022
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                allocated = min(rowSum[i], colSum[j])
                matrix[i][j] = allocated 
                rowSum[i] -= allocated 
                colSum[j] -= allocated 
        return matrix 