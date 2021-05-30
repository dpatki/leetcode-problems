# submitted 28/15/2021

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def mySort2(point):
            return abs(point[0] - rCenter) + abs(point[1] - cCenter)
        listicle = []
        for i in range(rows):
            for j in range(cols):
                listicle.append([i, j])  
      
        stuff = sorted(listicle, key=mySort2)
        return stuff
        