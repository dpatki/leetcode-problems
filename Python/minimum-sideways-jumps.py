#submitted 14/06/2022

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        top = 1
        middle = 0
        bottom = 1
        for rock in obstacles:
            if rock == 1:
                top = float("inf")
                middle = min(bottom + 1, top+1, middle)
                bottom = min(bottom, top+1, middle+1)
            elif rock == 2:
                middle = float("inf")
                top = min(top, bottom+1, middle+1)
                bottom = min(bottom, top+1, middle+1)
            elif rock == 3:
                bottom = float("inf")
                top = min(top, bottom+1, middle+1)
                middle = min(bottom + 1, top+1, middle)
            else:
                top = min(top, bottom+1, middle+1)
                middle = min(bottom + 1, top+1, middle)
                bottom = min(bottom, top+1, middle+1)
        return min(top, middle, bottom)