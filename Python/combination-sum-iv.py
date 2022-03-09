#submitted 07/03/2022
class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
        memos = [0]  * (target+1)
        memos[0] = 1
        for num in nums:
            for i in range(len(memos)):
                
                memos[i+num] += memos[i] 
            print(memos)
   
        return memos[-1]