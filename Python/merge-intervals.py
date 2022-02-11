#submitted 10/02/2022
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        test = sorted(intervals, key=lambda intervals: intervals[0])
        news = []
        start = test[0]
        i = 1
        while i < len(intervals):
            while i < len(intervals) and start[0] <= test[i][0] <= start[1]:
                start[1] = max(start[1], test[i][1])
                i += 1
            news.append(start)
            if i < len(intervals):
                start = test[i]
            i += 1
        if i == len(intervals):
            news.append(start)
        return news