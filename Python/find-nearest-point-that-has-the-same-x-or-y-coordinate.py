# submitted 01/08/2021

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best = -1
        dist = -1
        for i in range(len(points)):
            #print(i, points[i])
            if points[i][0] == x:
                if dist == -1:
                    dist = abs(y - points[i][1])
                    best = i
                elif abs(y - points[i][1]) < dist:
                    dist = abs(y - points[i][1])
                    best = i
            elif points[i][1] == y:
                if dist == -1:
                    dist = abs(x - points[i][0])
                    best = i
                elif abs(x - points[i][0]) < dist:
                    dist = abs(x - points[i][0])
                    best = i
                
            else:
                pass

        return best
