class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Recursive call, marks all visited locations on grid connected to input coordinate
        count = 0
        def expand(y: int, x: int):
            nonlocal count
            grid[y][x] = 0
            for ny, nx in [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]:
                if ny >= len(grid) or ny < 0 or nx >= len(grid[0]) or nx < 0:
                    continue
                if grid[ny][nx] == 1:
                    count += 1
                    expand(ny, nx)
                    grid[ny][nx] = 0
            return 

        res = 0
        # Each time land is found, update connecting land on grid to X and continue
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 1:
                    count += 1
                    expand(j, i)
                    res = max(res, count)
                    count = 0

        return res
                