#submitted 03/21/2021
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        i = 1
        listicle = []
        while i <= n:
            listicle.append(i)
            i+= 1
        return itertools.combinations(listicle, k)