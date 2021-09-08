#submitted 03/09/2021

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(coords):
            #print(coords)
            if coords[0] < 0 or coords[0] >= len(board) or coords[1] < 0 or coords[1] >= len(board[0]) or board[coords[0]][coords[1]] != 'O':
                return
            board[coords[0]][coords[1]] = '#'
            dfs([coords[0] - 1, coords[1]])
            dfs([coords[0] + 1, coords[1]])
            dfs([coords[0], coords[1] - 1])
            dfs([coords[0], coords[1] + 1])
        
        for i in range(len(board[0])):
            dfs([0, i])
            dfs([len(board) - 1, i])
        
        for i in range(1, len(board) - 1):
            dfs([i, 0])
            dfs([i, len(board[0]) - 1])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'