#submitted 02/14/2021
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = (len(mat)-1) + len(mat[0])
        m = len(mat)
        n = len(mat[0])
        onCol = len(mat[0]) - 1
        onRow = len(mat) - 1
        while diagonals > 0:
            things = []
            if onCol < 0:
                i = onRow
                j = 0
                while (i < m) and (j < n):
                    things.append(mat[i][j])
                    j += 1
                    i += 1
                things.sort()
                i = onRow
                j = 0
                for elem in things:
                    mat[i][j] = elem
                    i += 1
                    j += 1
                onRow -= 1
            else:
                i = 0
                j = onCol
                while (i < m) and (j < n):
                    things.append(mat[i][j])
                    i += 1
                    j += 1
                things.sort()
                i = 0
                j = onCol
                for elem in things:
                    mat[i][j] = elem
                    i += 1
                    j += 1
                onCol -= 1
            diagonals -= 1
        return mat
        