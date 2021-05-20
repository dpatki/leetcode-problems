#submitted 07/05/2021
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        stuff = []
        for elem in nums:
            if elem > 0 and elem not in stuff:
                stuff.append(elem)
        stuff.sort()
        if len(stuff) == 0:
            return 1
        if stuff[0] != 1:
            return 1
        for i in range(0, len(stuff)-1):
            if (stuff[i] + 1) != stuff[i+1]:
                return stuff[i] + 1
        return stuff[len(stuff) - 1] + 1