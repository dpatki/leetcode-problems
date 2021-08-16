#submitted 15/08/2021

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 or len(grid[0]) == 1:
            return 0
        
        que = []
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                grid[0][i] = 0
                if grid[1][i] == 1:
                    que.append([1, i])
            if grid[-1][i] == 1:
                grid[-1][i] = 0
                if grid[-2][i] == 1:
                    que.append([-2, i])
        for i in range(1, len(grid) -1):
            if grid[i][0] == 1:
                grid[i][0] = 0
                if grid[i][1] == 1:
                    que.append([i, 1])
            if grid[i][-1] == 1:
                grid[i][-1] = 0
                if grid[i][-2] == 1:
                    que.append([i, -2])
        
        while que:
            #print(grid)
            #print(que)
            element = que.pop(0)
           
            if grid[element[0]][element[1]] == 0:
                continue
            grid[element[0]][element[1]] = 0
            
            if grid[element[0] - 1][element[1]] == 1:
                que.append([element[0] - 1, element[1]])
            
            if grid[element[0] + 1][element[1]] == 1:
                que.append([element[0] + 1, element[1]])
            
            if grid[element[0]][element[1] - 1] == 1:
                que.append([element[0], element[1] - 1])
            
            if grid[element[0]][element[1] + 1] == 1:
                que.append([element[0], element[1] + 1])
        
        total = 0
        for row in grid:
            total += sum(row)
        
        return total