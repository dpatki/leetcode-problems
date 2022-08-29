#submitted 30/05/2022

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            #print(stack, temperatures[i])
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(0)
                stack.append((temperatures[i], i))
            else:
                res.append(stack[-1][1]-i)
                stack.append((temperatures[i], i))
        res.reverse()
        #print(res)
        return res