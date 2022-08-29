#submitted 23/08/2022

class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        power = 31
        while n > 0:
            if n - 2 ** power >= 0:
                n = n - 2 ** power
                total += 1
            power -= 1
        return total