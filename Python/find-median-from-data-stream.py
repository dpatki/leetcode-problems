#submitted 19/05/2022

class MedianFinder:

    def __init__(self):
        self.lefts = []
        self.rights = []
        self.total = 0

    def addNum(self, num: int) -> None:
        if not self.lefts:
            heapq.heappush(self.lefts, -num)
            self.total += 1
            return
        elif not self.rights:
            if num < -self.lefts[0]:
                temp = heapq.heappushpop(self.lefts, -num)
                heapq.heappush(self.rights, -temp)
            else:
                heapq.heappush(self.rights, num)
            self.total += 1
            return 
        if self.total % 2 == 0:
            if num > self.rights[0]:
                temp = heapq.heappushpop(self.rights, num)
                heapq.heappush(self.lefts, -temp)
            else:
                heapq.heappush(self.lefts, -num)
            self.total += 1
            return 
        else:
            if num < -self.lefts[0]:
                temp = heapq.heappushpop(self.lefts, -num)
                heapq.heappush(self.rights, -temp)
            else:
                heapq.heappush(self.rights, num)
            self.total += 1

    def findMedian(self) -> float:
        #print(self.lefts, self.rights, self.total)
        if self.total % 2 == 0:
            return (-self.lefts[0] + self.rights[0])/2
        return -self.lefts[0]
        

