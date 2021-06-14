#sumbitted 13/06/2021
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0

        def hasA1(stuffs):
            for row in stuffs:
                if 1 in row:
                    return True
            return False

        def count1s(matrix):
            count = 0
            for row in matrix:
                count += sum(row)
            #print(count, matrix)
            return count

        while hasA1(matrix):
            count += count1s(matrix)
            newmat = []
            for i in range(0, len(matrix) - 1):
                newrow = []
                for j in range(0, len(matrix[0])-1):
                    rowelem = 0
                    if (matrix[i][j] == 1) and ((matrix[i+1][j] == 1)) and (matrix[i][j+1] == 1) and (matrix[i+1][j+1] == 1):
                        rowelem = 1
                    newrow.append(rowelem)
                newmat.append(newrow)
            matrix = newmat
            #print(newmat)

        return count