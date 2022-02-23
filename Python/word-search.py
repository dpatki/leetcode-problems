#submitted 22/02/2022

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurse(board, word, x, y):
            if len(word) == 0:
                return True
            if board[x][y] != word[0]:
                return False
            chara = word[0]
            up = False
            down = False
            left = False
            right = False
            board[x][y] = "."
            if x > 0:
                left = recurse(board, word[1:], x-1, y)
            if x < len(board) - 1:
                right = recurse(board, word[1:], x+1, y )
            if y > 0:
                up = recurse(board, word[1:], x, y-1)
            if y < len(board[0]) - 1:
                down = recurse(board, word[1:], x, y+1 )
            board[x][y] = chara
            return up or down or left or right
        
        if len(board) == 1 and len(board[0]) == 1:
            return board[0][0] == word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    thing = recurse(board, word, i, j)
                    if thing:
                        return True
        
        return False