#submitted 16/08/2021
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 1 and len(board[0]) == 1:
            board[0][0] = 0
            return
        if len(board) == 1:
            nextstate = [0] * len(board[0])
            nextstate[0] = 0
            nextstate[-1] = 0
            for i in range(1, len(board[0]) - 1):
                if board[0][i-1] + board[0][i+1] == 2:
                    nextstate[i] = board[0][i]
                else:
                    nextstate[i] = 0
            board[0] = nextstate
            return
        if len(board[0]) == 1:
            nextstate = [0] * len(board)
            nextstate[0] = 0
            nextstate[-1] = 0
            for i in range(1, len(board) - 1):
                if board[i-1][0] + board[i+1][0] == 2:
                    nextstate[i] = board[i][0]
                else:
                    nextstate[i] = 0
            for i in range(len(nextstate)):
                board[i][0] = nextstate[i]
            return
            
        def updatecell(summ, alive):
            if summ < 2:
                return 0
            elif summ > 3:
                return 0
            elif summ == 3:
                return 1
            return alive
        
        
        nextstate = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        #print(board, nextstate)
        for i in range(1, len(board) - 1):
            for j in range (1, len(board[0]) - 1):
                #print(i, j)
                summ = board[i-1][j-1] + board[i-1][j] + board[i-1][j+1] + board[i][j-1] + board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
                nextstate[i][j] = updatecell(summ, board[i][j])
        
        for i in range(1, len(board[0]) - 1):
            summ = board[0][i-1] + board[0][i+1] + board[1][i-1] + board[1][i] + board[1][i+1]
            nextstate[0][i] = updatecell(summ, board[0][i])
            
            summ = board[-1][i-1] + board[-1][i+1] + board[-2][i-1] + board[-2][i] + board[-2][i+1]
            nextstate[-1][i] = updatecell(summ, board[-1][i])
            
        for j in range(1, len(board) - 1):
            summ = board[j+1][0] + board[j-1][0] + board[j+1][1] + board[j][1] + board[j-1][1]
            nextstate[j][0] = updatecell(summ, board[j][0])
            
            summ = board[j+1][-1] + board[j-1][-1] + board[j+1][-2] + board[j][-2] + board[j-1][-2]
            nextstate[j][-1] = updatecell(summ, board[j][-1])
            
        summ = board[0][1] + board[1][0] + board[1][1]
        nextstate[0][0] = updatecell(summ, board[0][0])
        
        summ = board[-2][0] + board[-2][1] + board[-1][1]
        nextstate[-1][0] = updatecell(summ, board[-1][0])
        
        summ = board[0][-2] + board[1][-2] + board[1][-1]
        nextstate[0][-1] = updatecell(summ, board[0][-1])
        
        summ = board[-1][-2] + board[-2][-2] + board[-2][-1]
        nextstate[-1][-1] = updatecell(summ, board[-1][-1])
        
        i = 0
        for row in nextstate:
            board[i] = row
            i += 1