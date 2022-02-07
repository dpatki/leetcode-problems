#submitted 03/02/2022
class Solution:
    def tribonacci(self, n: int) -> int:
        n1 = 0
        n2  = 1
        n3 = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(2, n):
            temp = n1 + n2 + n3
            
            n1 = n2
            n2 = n3
            n3 = temp
        return n3