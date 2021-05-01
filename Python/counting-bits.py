#submitted 03/04/2021
class Solution:
    def countBits(self, num: int) -> List[int]:
        thingy = [0]
        while len(thingy)-1 < num:
            temp = [1+elem for elem in thingy]
            thingy = thingy + temp
        
        if len(thingy)-1 ==  num:
            return thingy
        
        while len(thingy)-1 != num:
            thingy.pop()
            
        return thingy
            