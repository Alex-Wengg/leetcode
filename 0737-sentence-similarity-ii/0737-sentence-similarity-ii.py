class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        if len(words1) != len(words2):
            return False
        
        connections = defaultdict(set)
        for w1, w2 in pairs:
            connections[w1].add(w2)
            connections[w2].add(w1)
        
        roots = {}
        def dfs(word, root_word):
            if word in roots:
                return None
            roots[word] = root_word
            for connectedWord in connections[word]:
                dfs(connectedWord, root_word)
        
        for word in connections:
            dfs(word, word)
        
        for w1,w2 in zip(words1, words2):
            if roots.get(w1, w1) != roots.get(w2,w2):
                return False
        return True 