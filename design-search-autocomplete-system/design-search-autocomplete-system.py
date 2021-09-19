class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = {}
        self.hot = 0
    
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.searchTerm = ""
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])
			
    def add(self,sentence, hot):
        node = self.root
        for c in sentence: 
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
        node.hot-= hot
        
    def search(self):
        node = self.root
        res = []
        path = ""

        for c in self.searchTerm:
            if c not in node.children:
                return res
            path +=c
            node = node.children[c]
        self.dfs(node, path,res)
        return [item[1] for item in sorted(res)[:3]]
            
    def dfs(self,node, path, res):
        if node.isEnd:
            res.append((node.hot,path))
        for c in node.children:
            self.dfs(node.children[c], path+c,res)
            
    def input(self, c):
        if c != "#":
            self.searchTerm +=c
            return self.search()
        else:
            self.add(self.searchTerm, 1)
            self.searchTerm =""
        