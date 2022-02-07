#submitted 27/01/2022
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memos = [-1] * (amount + 1)
        memos[0] = 0
        for coin in coins:
            for i in range(len(memos)):
                if i-coin >= 0:
                    if memos[i] != -1 and memos[i-coin] != -1:
                        memos[i] = min(memos[i], memos[i - coin] + 1)
                    elif memos[i] == -1:
                        if memos[i-coin] != -1:
                            memos[i] = memos[i-coin] + 1
        print(memos)
        return memos[-1]
                    