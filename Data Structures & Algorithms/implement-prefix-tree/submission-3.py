class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        head = self.root
        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode()
            head = head.children[char]
        head.isEndOfWord = True
        return

    def search(self, word: str) -> bool:

        head = self.root
        for char in word:
            if char not in head.children:
                return False
            head = head.children[char]
        return head.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        
        head = self.root
        for char in prefix:
            if char not in head.children:
                return False
            head = head.children[char]
        return True
        