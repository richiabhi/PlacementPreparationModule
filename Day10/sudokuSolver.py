class Solution:
    def solveSudoku(self, board) -> None:
        for row in range(0, 9):
            for col in range(0, 9):
                if(board[row][col] == "."):
                    for i in range(1, 10):
                        if(self.isValid(row, col, i, board)):
                            board[row][col] = str(i)
                            if(self.solveSudoku(board) == True):
                                return True
                            else:
                                board[row][col] = "."
                    return False
        return True

    def isValid(self, row, col, i, board):
        for c in range(0, 9):
            if(board[row][c] == str(i)):
                return False
            if(board[c][col] == str(i)):
                return False
            if(board[3*(row//3)+(c//3)][3*(col//3)+(c % 3)] == str(i)):
                return False
        return True
