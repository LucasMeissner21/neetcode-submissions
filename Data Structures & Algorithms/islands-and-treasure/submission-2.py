class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        # Add all treasure coordinates to queue
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.pop(0)   
            # Check all adjacent cells         
            for nr, nc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                # Ensure border cases are ignored
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                # Only append cells that haven't been traversed and are traversible
                if grid[nr][nc] == 2147483647:
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[row][col] + 1

        return
