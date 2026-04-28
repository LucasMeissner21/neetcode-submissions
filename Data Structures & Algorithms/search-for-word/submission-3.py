class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Solution 1: Iterate and check
        x = len(board[0]) - 1
        y = len(board) - 1
        queue = []

        def checkNeighbors(target: str, coord: tuple(int, int)) -> list(tuple(int, int)):
            nonlocal x
            nonlocal y
            res = []
            if coord[0] > 0 and board[coord[0] - 1][coord[1]] == target:
                res.append((coord[0] - 1, coord[1]))
            if coord[0] < y and board[coord[0] + 1][coord[1]] == target:
                res.append((coord[0] + 1, coord[1]))
            if coord[1] > 0 and board[coord[0]][coord[1] - 1] == target:
                res.append((coord[0], coord[1] - 1))
            if coord[1] < x and board[coord[0]][coord[1] + 1] == target:
                res.append((coord[0], coord[1] + 1))
            return res

        path = set()

        def checkExistence(index: int, coord: tuple(int, int)) -> bool:
            if index == len(word) - 1:
                return True
            neighbors = checkNeighbors(word[index + 1], coord)
            for neighbor in neighbors:
                if neighbor in path:
                    continue
                path.add(neighbor)
                if checkExistence(index + 1, neighbor):
                    return True
                path.remove(neighbor)
            return False

        for i in range(y + 1):
            for j in range(x + 1):
                if board[i][j] == word[0]:
                    path.add((i, j))
                    if checkExistence(0, (i, j)):
                        return True
                    path.remove((i, j))

        return False


            

            