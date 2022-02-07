#submitted 01/02/2022
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapq.heapify(piles)
        for i in range(k):

            item = heapq.heappop(piles)
            item *= -1
            item = item - item//2
            item *= -1
            heapq.heappush(piles, item) 
            #print(piles)

        return sum(piles) * -1