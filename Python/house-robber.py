#submitted 01/02/2022
class Solution:
    def rob(self, nums: List[int]) -> int:
        memos = [0]*(len(nums)+1)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        memos[1] = nums[0]
        for i in range(1, len(nums)):
            memos[i+1] = max(nums[i] + memos[i-1], memos[i])
        #print(memos)
        return memos[-1]