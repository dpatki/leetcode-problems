#submitted 25/02/2022

class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = Counter(s)
        h = []
        for elem in (list(letters)):
            heapq.heappush(h, (-letters[elem], elem))
        stringify = ""
        cur = (heapq.heappop(h))
        while h:
            #print(cur, stringify)
            elem = cur 
            cur = heapq.heappop(h)
            stringify += elem[1]
            if elem[0] != -1:
                heapq.heappush(h, (elem[0]+1, elem[1]))
        if cur[0] == -1:
            stringify += cur[1]
            return stringify 
        return ""
            