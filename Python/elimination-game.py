#submitted 29/08/2021

class Solution:
    def lastRemaining(self, n: int) -> int:
        i = 0
        mini = 1
        while n > 1:
            #print(mini, i, n)
            if n % 2 == 1 and i % 2 == 1:
                #inc min
                mini += 2 ** i
            elif i % 2 == 0:
                #inc min
                mini += 2 ** i

            i += 1
            n = n // 2

        return mini