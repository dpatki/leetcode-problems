#submitted 26/03/2021
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        temp = 0
        for i in range(1, int(math.sqrt(area) +1)):
            if area % i == 0:
                temp = i
  
        return [int(area/temp), temp]