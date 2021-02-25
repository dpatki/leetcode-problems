#submitted 01/31/2021
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix) * len(matrix[0])
        m = len(matrix[0])
        n = len(matrix)
        if m == 1 and n == 1:
            if (matrix[0][0] != target):
                return False
            else: 
                return True
        start = 0
        end = length 
        while (start <= end):
            mid = (start+end) // 2
            print(mid)
            quot = mid // m
            rem = mid % m
            if (mid == 0):
                quot = 0
                rem = 0
            else:      
                if (rem == 0):
                    quot -= 1
                    rem = m - 1
                else:
                    rem -= 1
            print(matrix[quot][rem])
            if (matrix[quot][rem] == target):
                return True
            elif (matrix[quot][rem] > target):
                end = mid - 1
            else:
                start = mid + 1
        
        return False
        