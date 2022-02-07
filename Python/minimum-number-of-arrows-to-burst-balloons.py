#submitted 20/01/2022
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        test = sorted(points, key=lambda points: points[1])
        arrow = test[0][1]
        count = 1
        #print(test)
        for elem in test:
            if not(elem[0] <= arrow <= elem[1]):
                count += 1
                arrow = elem[1]
            
        
        return count