class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False  # also add end marker for correctness

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        head = self.root                      # Fix 1: use local variable
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode()
            head = head.children[c]
        head.endOfWord = True
        return

    def search(self, word: str, node=None) -> bool:
        if node is None:
            node = self.root                  # Fix 1: default to root, no instance state
        for i in range(len(word)):
            if word[i] == ".":
                for child in node.children.values():
                    if self.search(word[i + 1:], child):  # Fix 2: return if match found
                        return True
                return False                  # Fix 2: no branch matched
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.endOfWord                 # check word ends here, not just mid-trie
