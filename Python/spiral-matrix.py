#submitted 18/06/2021
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0 or cols == 0:
            return []
        
        final = []
        for elem in matrix[0]:
            final.append(elem)
        
        if rows == 1:
            return final
        
        final.pop()
        
        for i in range(rows):
            final.append(matrix[i][cols - 1])
        
        if cols == 1:
            return final
        
        final.pop()
        
        for i in range(cols -1, -1, -1):
            final.append(matrix[rows -1][i])
        
        if rows == 2:
            return final
        
        final.pop()
        for i in range(rows -1, 0, -1):
            final.append(matrix[i][0])
        
        newmat = []
        for i in range(1, rows - 1):
            newmat.append(matrix[i][1:cols-1])
            
        final += self.spiralOrder(newmat)
        
        return final