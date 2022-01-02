#submitted 10/09/2021
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        actual = 0
        i = 1
        while (n - (i * 9 * (10**(i-1)))) > 0:
            #print(actual, i)
            n -= (i * 9 * (10**(i-1)))
            actual +=  9 * (10**(i-1))
            i += 1
        #print(actual, i)
        actual += ((n-1) // i) +1
        index  = (n-1) % i
        #print(actual, index)
        stringy = str(int(actual))
        return int(stringy[index])