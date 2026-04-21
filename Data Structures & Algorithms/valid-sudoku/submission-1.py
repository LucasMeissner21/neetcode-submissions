class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row Checking
        rows = collections.defaultdict(set)

        # Col Checking
        cols = collections.defaultdict(set)

        # Squares Checking
        squares = collections.defaultdict(set) # key = (c/3, r/3) int div

        # Iterate through values, check if already exist in any hashset, otherwise add to all correct hashsets
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                # If already present in any set, return false
                if (val in rows[r] or val in cols[c] or val in squares[c//3, r//3]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[c//3, r//3].add(val)
        
        return True