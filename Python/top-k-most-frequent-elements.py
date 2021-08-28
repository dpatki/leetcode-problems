#submitted 25/08/2021

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        
        for elem in nums:
            c[elem] += 1
        
        thing = c.most_common(k)
        res = []
        for elem in thing:
            res.append(elem[0])
        return res
        