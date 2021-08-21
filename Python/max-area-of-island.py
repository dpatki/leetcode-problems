#submitted 18/08/2021
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def nameisland(coords, name):
            if coords[0] < 0 or coords[1] < 0 or coords[0] >= len(grid) or coords[1]>=len(grid[0]) or grid[coords[0]][coords[1]] != 1:
                return

            grid[coords[0]][coords[1]] = name
            nameisland([coords[0] - 1, coords[1]], name)
            nameisland([coords[0] + 1, coords[1]], name)
            nameisland([coords[0], coords[1] - 1], name)
            nameisland([coords[0], coords[1] + 1], name)
                
            
        i = 2
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                #print(j, k)
                if grid[j][k] == 1:
                    nameisland([j, k], i)
                    i += 1
        
        #print(grid)
        c = Counter()
        isIsland = False
        
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                stuff = grid[j][k]
                if stuff != 1 and stuff != 0:
                    isIsland = True
                    c[stuff] += 1
        
        
        if not isIsland:
            return 0
        
        #print(c.most_common(1))
        
        return (c.most_common(1)[0][1])
                