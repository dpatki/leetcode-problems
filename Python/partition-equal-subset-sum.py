#submitted 02/03/2022
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 == 1:
            return False 
        memos = [False for _ in range(summ//2+1)]
        memos[0] = True
        for elem in nums:
            #print(memos)
            for i in range(len(memos)-1, -1, -1):
                if memos[i] and elem + i < len(memos):
                    memos[i+elem] = True
            if memos[-1]:
                return True
        
        return False