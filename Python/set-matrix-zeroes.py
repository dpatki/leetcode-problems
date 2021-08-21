#submitted 20/08/2021
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        for elem in rows:
            matrix[elem] = [0] * len(matrix[0])
        
        for elem in cols:
            for i in range(len(matrix)):
                matrix[i][elem] = 0
        