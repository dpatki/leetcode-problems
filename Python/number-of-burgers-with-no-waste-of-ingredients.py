#submitted 01/03/2021
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if not tomatoSlices % 2 == 0:
            return []
        if cheeseSlices == 0 and tomatoSlices == 0:
            return [0,0]
        x = tomatoSlices/2 - cheeseSlices
        if x < 0:
            return []
        y = cheeseSlices - x
        if y < 0:
            return []
        return [x, y]
                