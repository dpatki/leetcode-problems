#submitted 09/02/2022
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        news = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            news.append(intervals[i])
            i+= 1
        #print(intervals[i], newInterval)
        if i < len(intervals) and intervals[i][0] <= newInterval[0] <= intervals[i][1]:
            newInterval[0] = intervals[i][0]
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        while i < len(intervals) and newInterval[0] <= intervals[i][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        news.append(newInterval)
        
        while i < len(intervals):
            news.append(intervals[i])
            i += 1
        
        return news
        