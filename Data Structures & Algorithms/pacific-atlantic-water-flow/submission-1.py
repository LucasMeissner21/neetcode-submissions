class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r = len(heights) # num rows
        c = len(heights[0]) # num columns
        pacific = set()
        atlantic = set()
        # Get row borders in pacific and atlantic
        for i in range(c):
            pacific.add((0, i)) 
        for i in range(c):
            atlantic.add((r - 1, i))
        for j in range(r):
            pacific.add((j, 0)) 
        for j in range(r):
            atlantic.add((j, c - 1))

        def checkFlow(row: int, col: int) -> bool:
            
            visited = set()
            atl = False
            pac = False
            if (row, col) in pacific:
                pac = True
            if (row, col) in atlantic:
                atl = True
            queue = [(row, col)]
            while queue and not (atl and pac):
                row, col = queue.pop(0)
                for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if nr < 0 or nr >= r or nc < 0 or nc >= c:
                        continue
                    if heights[nr][nc] > heights[row][col] or (nr, nc) in visited:
                        continue
                    if (nr, nc) in pacific:
                        pac = True
                    if (nr, nc) in atlantic:
                        atl = True
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            return pac and atl

        res = []
        for j in range(r):
            for i in range(c):
                if checkFlow(j, i):
                    res.append([j, i])
        return res


