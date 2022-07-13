class Solution:
    def solveNQueens(self, n: int):
        def isSafe(row, col, board):
            copyrow = row
            copycol = col
            while(row >= 0 and col >= 0):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row = copyrow
            col = copycol
            while(col >= 0):
                if board[row][col] == "Q":
                    return False
                col -= 1

            row = copyrow
            col = copycol
            while(col >= 0 and row <= n-1):
                if board[row][col] == "Q":
                    return False
                col -= 1
                row += 1
            return True

        def solveNQueens2(col, board):
            if col == len(board):
                res.append(["".join(i) for i in board])
                return
            for row in range(n):
                if isSafe(row, col, board):
                    board[row][col] = "Q"
                    solveNQueens2(col+1, board)
                    board[row][col] = "."

        res = []
        board = [["." for _ in range(n)]for _ in range(n)]
        solveNQueens2(0, board)
        return res
