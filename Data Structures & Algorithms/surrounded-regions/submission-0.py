class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Find an O, store all connected O's, if a border is hit don't change, otherwise
        # change

        visited = set()
        O = set()
        flip = True

        def getConnected(row: int, col: int):
            nonlocal flip, O
            if (row, col) in visited:
                return
            O.add((row, col))
            visited.add((row, col))
            for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    flip = False
                    continue
                if board[nr][nc] == 'O':
                    getConnected(nr, nc)
            return

        def flipAll(coords: set):
            for r, c in coords:
                board[r][c] = 'X'
            return

        for row in range(1, len(board) - 1): # Only check inside border
            for col in range(1, len(board[0]) - 1):
                if board[row][col] == 'O' and (row, col) not in visited:
                    O.clear()
                    flip = True
                    getConnected(row, col)
                    if flip:
                        flipAll(O)
                

        return

        