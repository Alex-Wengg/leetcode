class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.c = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for w in word:
            if w not in node.c:
                node.c[w] = Trie()
            node = node.c[w]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for w in word:
            if w not in node.c:
                return None
            node = node.c[w]
        if node and node.end:
            return True
        return False
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for w in prefix:
            if w not in node.c:
                return None
            node = node.c[w]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)