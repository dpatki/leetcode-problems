#submitted 03/02/2022
class Solution:
    def fib(self, n: int) -> int:
        n1 = 0
        n2  = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(1, n):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2