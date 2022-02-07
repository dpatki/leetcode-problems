#submitted 05/02/2022
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        stuff = [0] * max(nums)
        things = Counter(nums)
        for elem in list(things):
            stuff[elem-1] = elem * things[elem]
        memos = [0]*(len(stuff)+1)
        if len(stuff) == 1:
            return stuff[0]
        if len(stuff) == 2:
            return max(stuff[0], stuff[1])
        memos[1] = stuff[0]
        for i in range(1, len(stuff)):
            memos[i+1] = max(stuff[i] + memos[i-1], memos[i])
        #print(memos)
        return memos[-1]