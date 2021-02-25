#submitted 01/07/2021
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n%3 == 0:
            return int(3 ** (n/3))
        elif n%3 == 1:
            return int(4 * (3 ** ((n//3) -1)))
        else:
            return int(2 * (3 ** (n//3)))