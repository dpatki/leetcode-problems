#submitted 16/05/2021
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def mySort(point):
            return (point[0]**2 + point[1]**2)
        
        stuff = sorted(points, key=mySort)
        return stuff[:k]