class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Very very slow
        r = len(heights) # num rows
        c = len(heights[0]) # num columns
        pacific = []
        atlantic = []
        visited = set()
        visited2 = set()
        res = set()

        res.add((0, c - 1))
        res.add((r - 1, 0))

        # Get row borders in pacific and atlantic queues
        for i in range(c):
            pacific.append((0, i)) 
        for i in range(c):
            atlantic.append((r - 1, i))
        for j in range(r):
            pacific.append((j, 0))
        for j in range(r):
            atlantic.append((j, c - 1))

        # Pass 1: Add all cells flowing into pacific to visited
        while pacific:
            row, col = pacific.pop(0)
            for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if nr < 0 or nr >= r or nc < 0 or nc >= c:
                    continue
                if heights[nr][nc] >= heights[row][col] and (nr, nc) not in visited:
                    pacific.append((nr, nc))
                    visited.add((nr, nc))

        # Pass 2: Add all cells flowing into atlantic, if already in visited add to res
        while atlantic:
            row, col = atlantic.pop(0)
            for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if nr < 0 or nr >= r or nc < 0 or nc >= c:
                    continue
                if heights[nr][nc] >= heights[row][col] and (nr, nc) not in visited2:
                    atlantic.append((nr, nc))
                    if (nr, nc) in visited:
                        res.add((nr, nc))
                    visited2.add((nr, nc))

        return [[row, col] for row, col in res]
        
