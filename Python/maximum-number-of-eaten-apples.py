#submitted 05/23/2021

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        q = []
        counter = 0
        i = 0
        while i < len(apples) or q:
            #print(q)
            if i < len(apples) and apples[i] != 0:
                heapq.heappush(q,[i + days[i], apples[i]])
            while q and (q[0][0] <= i or q[0][1] == 0):
                heapq.heappop(q)
            if q:
                #print(q[0])
                q[0][1] -= 1
                counter += 1
            i += 1

        #print(q)
        return counter