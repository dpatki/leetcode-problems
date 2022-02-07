#submitted 15/01/2022
class Solution:
    best = 0
    def totalFruit(self, fruits: List[int]) -> int:
        current = []
        new = 0
        start = 0
        end = 0
        while start < len(fruits):
            if len(current) < 2 and fruits[start] not in current:
                current.append(fruits[start])
                new = start
                start += 1
            elif fruits[start] in current:
                start += 1
            else:
                end = new
                start = new
                current = [fruits[start]]
            if start - end >  self.best:
                self.best = start - end
        
        return self.best