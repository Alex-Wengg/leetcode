class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        parent = {}

        def find(w):
            if w not in parent:
                parent[w] = w
            while w in parent and parent[w] != w:
                w = parent[w]
            return w
        
        for a, b in pairs:
            a1 = find(a)
            b1 = find(b)
            parent[a1] = b1
        
        l1 = len(words1)
        l2 = len(words2)
        if l1 != l2:
            return False
        
        for i in range(l1):
            a, b = find(words1[i]), find(words2[i])
            if a != b:
                return False
        return True