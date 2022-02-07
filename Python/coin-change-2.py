#submitted 25/01/2022
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        memos = [0 for i in range(amount+1)]

        memos[0] = 1

        for i in range(len(coins)):
            for j in range(len(memos)):
                if j - coins[i] >= 0:
                    memos[j] += memos[j - coins[i]] 
          
        return memos[-1]