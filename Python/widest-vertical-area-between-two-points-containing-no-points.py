#submitted 15/02/2022
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        stuff = sorted(points, key = lambda points: points[0])
        maxDiff = 0
        for i in range(0, len(stuff)-1):
            maxDiff = max(maxDiff, stuff[i+1][0] - stuff[i][0])
        return maxDiff