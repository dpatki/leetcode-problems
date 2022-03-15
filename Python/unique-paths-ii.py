#submitted 09/03/2022

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i]:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
                
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0]:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] =  obstacleGrid[i-1][0]
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        print(obstacleGrid)
        return obstacleGrid[-1][-1]