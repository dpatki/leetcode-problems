#submitted 04/02/2022
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        memos = [0]*n
        memos[0] = 1
        memos[1] = 2
       
        for i in range(2, n):
            memos[i] = memos[i-1] + memos[i-2]
        return memos[-1]