#submitted 01/01/2021
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while (low <= high):
            m = low + ((high-low))/2
            if (isBadVersion(m)):
                if m == 1:
                    return m
                elif(not isBadVersion(m-1)):
                    return m
                else:
                    high = m - 1
            if(not isBadVersion(m)):
                if (isBadVersion(m+1)):
                    return m+1
                else:
                    low = m+1
                
        