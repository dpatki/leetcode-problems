#submitted 24/05/2022

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sortFunction(a, b):
            first = str(a)
            second = str(b)
            if int(first+second) > int(second+first):
                return 1
            elif int(first+second) == int(second+first):
                return 0
            return -1
        
        sorts = sorted(nums, key=cmp_to_key(sortFunction), reverse=True)
        
        done = ""
        for elem in sorts:
            done += str(elem)
        return str(int(done))