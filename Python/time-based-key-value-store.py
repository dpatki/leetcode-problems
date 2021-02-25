#submitted 01/09/2021
class TimeMap:

    def __init__(self):
            """
            Initialize your data structure here.
            """
            self.jank = {}
            self.counter = 0

    def set(self, key, value, timestamp):
            """
            :type key: str
            :type value: str
            :type timestamp: int
            :rtype: None
            """
            if key not in self.jank:
                self.jank[key] = [[timestamp, value]]

            else:
                self.jank[key].append([timestamp, value])

            self.counter += 1

            #[1, {cam1: potato}] [1, {cam2: iguana}]
            #[1, {cam1: potato, cam2: iguana}]


    def get(self, key, timestamp):
            """
            :type key: str
            :type timestamp: int
            :rtype: str
            """
            if key not in self.jank:
                return ""
            #print(self.jank)
            if self.jank[key][0][0] > timestamp:
                 return ""
            # [1, 2], [3, 4], [5, 6]
            left = 0
            right = len(self.jank[key])
        
            while left < right:
                mid = (left + right) // 2
                if self.jank[key][mid][0] <= timestamp:
                    left = mid + 1
                elif self.jank[key][mid][0] > timestamp:
                    right = mid

            return "" if right == 0 else self.jank[key][right - 1][1]
            #print(high)
            #while low <= high:
            #    m = (high+low)//2
                
            #    if self.jank[key][m][0] == timestamp:
            #        print("sup")
            #        return self.jank[key][m][1]
            #    if self.jank[key][m][0] > timestamp:
            #        high = m
            #    else: 
            #        low = m +1

            #if high == 0:
            #    return ""
            #else:
            #    return self.jank[key][high - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)