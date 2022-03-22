#submitted 21/03/2022
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        h = []
        for elem in list(c):
            heapq.heappush(h, (-c[elem], elem))
        res = []
        for _ in range(k):
            elem = heapq.heappop(h)
            res.append(elem[1])
        return res