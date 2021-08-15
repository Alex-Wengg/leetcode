class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.word = False
        

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            if curr and curr.word:
                return True
            return False
        return dfs(0, self)


 