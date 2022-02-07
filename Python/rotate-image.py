#submitted 01/02/2022
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        #print(matrix)
        for j in range(len(matrix)):
            for i in range(j, len(matrix[0])):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        #print(matrix)