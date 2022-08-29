#submitted 27/04/2022

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == [[0]]:
            return 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        minute = 0
        while queue:
            secondary = []
            for elem in queue:
                i = elem[0]
                j = elem[1]
                if elem[0] > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    secondary.append((i-1, j))
                if elem[1] > 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    secondary.append((i, j-1))
                if elem[0] < len(grid) - 1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    secondary.append((i+1, j))
                if elem[1] < len(grid[0]) - 1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    secondary.append((i, j+1))
            queue = secondary
            minute += 1
        
        for row in grid:
            print(row)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        if minute == 0:
            return 0
       
        return minute -1
                    