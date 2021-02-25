#submitted 01/06/2021
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        current = Y
        ops = 0
        while current > X:
            if current % 2 == 0:
                current /= 2
                ops += 1
            else:
                current += 1
                ops += 1
        
        
        return int(ops + (X - current))