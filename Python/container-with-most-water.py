#submitted 01/29/2021
class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        best = 0
        while (first < last):
            current = min(height[first], height[last]) * (last - first)
            print(current)
            if current > best:
                best = current
            if height[first] > height[last]:
                last -= 1
            else:
                first += 1
        
        return best