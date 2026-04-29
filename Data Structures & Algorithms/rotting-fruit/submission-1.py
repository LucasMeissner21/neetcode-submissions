class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = set()
        # Add all treasure coordinates to queue
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh.add((row, col))
        
        if not fresh:
            return 0

        time = 0

        while queue:
            row, col = queue.pop(0)   
            # Check all adjacent cells         
            for nr, nc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                # Ensure border cases are ignored
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                # Only append cells that haven't been traversed and are traversible
                if grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    fresh.remove((nr, nc))
                    grid[nr][nc] = grid[row][col] + 1
                    time = max(grid[nr][nc], time)

        return time - 2 if not fresh else -1