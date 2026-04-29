class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores complete word at terminal node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie from word list
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(node: TrieNode, r: int, c: int, visited: set):
            ch = board[r][c]
            if ch not in node.children:
                return
            next_node = node.children[ch]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # avoid duplicates

            visited.add((r, c))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(next_node, nr, nc, visited)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(root, r, c, set())

        return res

        