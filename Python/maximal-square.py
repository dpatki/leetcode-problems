#submitted 05/23/2021
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        count = 0
        def hasA1(stuffs):
            for row in stuffs:
                if "1" in row:
                    return True
            return False
        while hasA1(matrix):
            newmat = []
            for i in range(0, len(matrix) - 1):
                newrow = []
                for j in range(0, len(matrix[0])-1):
                    rowelem = "0"
                    if (matrix[i][j] == "1") and ((matrix[i+1][j] == "1")) and (matrix[i][j+1] == "1") and (matrix[i+1][j+1] == "1"):
                        rowelem = "1"
                    newrow.append(rowelem)
                newmat.append(newrow)
            #print(newmat)
            matrix = newmat
            count += 1
        
        return count**2