class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = []  # queens[row] = col where queen is placed
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def buildBoard():
            board = []
            for row in range(n):
                line = ""
                for col in range(n):
                    line += "Q" if queens[row] == col else "."
                board.append(line)
            return board

        def recursion(row: int):
            if row == n:
                res.append(buildBoard())
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                queens.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                recursion(row + 1)
                queens.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        recursion(0)
        return res