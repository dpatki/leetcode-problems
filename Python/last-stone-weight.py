#submitted 01/10/2021
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            big = max(stones)
            stones.remove(big)
            second = max(stones)
            stones.remove(second)
            if (big - second != 0):
                stones.append(big-second)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]