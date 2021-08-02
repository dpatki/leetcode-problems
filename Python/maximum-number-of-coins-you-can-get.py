# submitted 23/07/2021

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        while piles:
            piles.pop()
            total += piles.pop()
            piles.pop(0)
        return total