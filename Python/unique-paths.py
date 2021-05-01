#submitted 02/04/2021
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            matrix[0][j] = 1
        for i in range(m):
            matrix[i][0] = 1
            
        for a in range(1,m):
            for b in range(1,n):
                matrix[a][b] = matrix[a-1][b] + matrix[a][b-1]
                
        return matrix[m-1][n-1]
                