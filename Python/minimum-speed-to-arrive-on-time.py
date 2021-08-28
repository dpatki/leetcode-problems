#submitted 27/08/2021
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if (len(dist) -1) >= hour:
            print("one")
            return -1

        
        
        def helper(speed):
            clock = 0
            for i in range(len(dist) - 1):
                clock += math.ceil(dist[i]/speed)
            clock += dist[len(dist) - 1]/speed

            if clock <= hour:
                return True
            return False
        
        if len(dist) == 1:
            stuff = (dist[0]/hour)
            if helper(int(stuff)):
                return int(stuff)
            return math.ceil(dist[0]/hour)
        
        test = max(dist[0: (len(dist) - 1)])
        second = math.ceil(dist[len(dist) - 1] / (hour - (len(dist) - 1)))
        end = max(test, second)
        start = 1
        
        while start <= end:
            test = (start + end) // 2
            #print(start, end, test)
            if helper(test):
                end = test - 1
            else:
                start = test + 1

        return start