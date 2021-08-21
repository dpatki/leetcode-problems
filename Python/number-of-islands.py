#accepted 17/08/2021
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def nameisland(coords):
            if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(grid) or coords[1]>=len(grid[0]) or grid[coords[0]][coords[1]] != '1':
                return
            
            grid[coords[0]][coords[1]] = '#'
            nameisland([coords[0] - 1, coords[1]])
            nameisland([coords[0] + 1, coords[1]])
            nameisland([coords[0], coords[1] - 1])
            nameisland([coords[0], coords[1] + 1])
                
            
        i = 0
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                #print(j, k)
                if grid[j][k] == '1':
                    nameisland([j, k])
                    i += 1
        
        return i
                