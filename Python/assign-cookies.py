#submitted 01/08/2021
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        total = 0
        if len(s) == 0 or len(g) == 0:
            return 0
        g.sort()
        s.sort()
        index = 0
        for child in g:
            if index > len(s) - 1:
                return total
            while s[index] < child:
                if index ==len(s) - 1:
                    return total
                index += 1
                
            total += 1
            index += 1
        return total