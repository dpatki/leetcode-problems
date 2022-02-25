#submitted 24/02/2022

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def traverse(i, j, parent, ocean):
            if heights[i][j] < parent or ocean[i][j] == 1:
                return
            ocean[i][j] = 1
            if i > 0:
                traverse(i-1, j, heights[i][j], ocean)
            if i < len(ocean)-1:
                traverse(i+1, j, heights[i][j], ocean)
            if j > 0:
                traverse(i, j-1, heights[i][j], ocean)
            if j < len(ocean[0])-1:
                traverse(i, j+1, heights[i][j], ocean)
                
        
        m = len(heights)
        n = len(heights[0])
        
        pacific = [[0]*n for i in range(m)]
        atlantic = [[0]*n for i in range(m)]
        
        for i in range(m):
            traverse(i, 0, -1, pacific)
            traverse(i, n-1, -1, atlantic)
        
        for i in range(n):
            traverse(0, i, -1, pacific)
            traverse(m-1, i, -1, atlantic)
            
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res