#submitted 08/03/2022
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def backtrack(current):
            for i in range(0, 10):
                if abs(int(current[-1]) - i) == k:
                    if len(current) == n-1:
                        result.append(int(current+str(i)))
                    else:
                        backtrack(current + str(i))
        for i in range(1, 10):
            backtrack(str(i))
        return result 