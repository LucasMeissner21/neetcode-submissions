class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Recursive call, marks all visited locations on grid connected to input coordinate
        def expand(y: int, x: int):
            grid[y][x] = "X"
            for ny, nx in [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]:
                if ny >= len(grid) or ny < 0 or nx >= len(grid[0]) or nx < 0:
                    continue
                if grid[ny][nx] == "1":
                    expand(ny, nx)
                grid[ny][nx] = "X"
            return 

        k = 0
        # Each time land is found, update connecting land on grid to X and continue
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == "1":
                    expand(j, i)
                    k += 1

        return k
                