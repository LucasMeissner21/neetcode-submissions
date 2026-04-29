class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        head = self.root
        for char in word:
            if not head.children[ord(char) - ord("a")]:
                head.children[ord(char) - ord("a")] = TrieNode()
            head = head.children[ord(char) - ord("a")]
        head.isEndOfWord = True
        return

    def search(self, word: str) -> bool:

        head = self.root
        for char in word:
            if not head.children[ord(char) - ord("a")]:
                return False
            head = head.children[ord(char) - ord("a")]
        return head.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        
        head = self.root
        for char in prefix:
            if not head.children[ord(char) - ord("a")]:
                return False
            head = head.children[ord(char) - ord("a")]
        return True
        