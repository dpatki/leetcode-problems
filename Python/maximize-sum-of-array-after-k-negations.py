#return 01/01/2021
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = 0
        k = K
        while k > 0:
            if A[i] < 0:
                A[i] = -A[i]
                i += 1 
            elif A[i] == 0:
                return sum(A)
            else:
                if i == 0:
                    if k % 2 == 0:
                        return sum(A)
                    else:
                        A[i] = -A[i]
                        return sum(A)
                else:
                    if min(A[i], A[i-1]) == A[i]:
                        if k % 2 == 0:
                            return sum(A)
                        else:
                            A[i] = -A[i]
                            return sum(A)
                    else:
                        if k % 2 == 0:
                            return sum(A)
                        else:
                            A[i-1] = -A[i-1]
                            return sum(A)
            k -= 1
        return sum(A)