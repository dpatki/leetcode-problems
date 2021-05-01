#submitted 02/04/2021
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix = [[-1 for i in range(len(isWater[0]))] for j in range(len(isWater))]
        queue = []
        for j in range(len(isWater)):
            for i in range(len(isWater[0])):
                if isWater[j][i] == 1:
                    matrix[j][i] = 0
                    queue.append([j, i])
      # iterate through as long as at least one elem is -1
      # during each iter, find the max possible height for elem
      # so long as that elem is not surrounded by all -1
      # repeat
        hasneg = False
        for lists in matrix:
            for elem in lists:
                if elem == -1:
                    hasneg = True

        if not hasneg:
            return matrix
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while (len(queue) != 0):
            thingy = queue.pop(0)
            for elem in dirs:
                height = thingy[0] + elem[0] 
                length = thingy[1] + elem[1]
                if 0 <= height and height < len(matrix):
                    if 0 <= length and length < len(matrix[0]):
                        if matrix[height][length] == -1:
                            matrix[height][length] =  matrix[thingy[0]][thingy[1]] + 1
                            queue.append([height, length])

        return matrix