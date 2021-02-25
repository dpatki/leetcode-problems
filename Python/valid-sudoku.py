#submitted 12/27/2020
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check cols
        for x in range(9):
            tempdict = {}
            for y in range(9):   
                #print(temparr)
                #print(board[x][y])
                #print(tempdict)
                if board[y][x] in tempdict:
                    if board[y][x] != '.':
                        #print("colfail at " + str(x) + str(y))
                        return False
                tempdict[board[y][x]] = 1
        #check rows
        for y in range(9):
            tempdict = {}
            for x in range(9):  
                #print(board[y][x])
                #print(tempdict) 
                if board[y][x] in tempdict:
                    if board[y][x] != '.':
                        #print("rowfail at " + str(y) + str(x))
                        return False
                tempdict[board[y][x]] = 1
        #check squares
        for alpha in range(3):
            for beta in range(3):    
                tempdict = {}
                for y in range(3*alpha, 3*alpha + 3):
                    for x in range(3*beta, 3*beta + 3):
                        #print(board[y][x])
                        #print(tempdict) 
                        if board[y][x] in tempdict:
                            if board[y][x] != '.':
                                #print("squarefail at " + str(y) + str(x))
                                return False
                        tempdict[board[y][x]] = 1
        return True

        