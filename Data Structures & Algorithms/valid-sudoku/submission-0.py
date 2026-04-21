class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Checking
        rows = collections.defaultdict(set)

        # Col Checking
        cols = collections.defaultdict(set)

        # Squares Checking
        squares = collections.defaultdict(set) # key = (c/3, r/3) int div

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in rows[r] or val in cols[c] or val in squares[int(c/3), int(r/3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[int(c/3), int(r/3)].add(val)
        
        return True