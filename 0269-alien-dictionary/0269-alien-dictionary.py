class Solution:
    def alienOrder(self, words):
        # a -> b
        adj = defaultdict(set)
        
        # in-de gree construction
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0 
        # adjList construction
        for i in range(len(words)-1):
            is_prefix = True
            w1 = words[i]
            w2 = words[i+1]
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    continue
                
                if c2 not in adj[c1]:
                    indegree[c2] += 1
                
                is_prefix = False
                adj[c1].add(c2)
                break 

            if is_prefix == True and len(w1) > len(w2):
                return ""


        # sort by inde gree, traversed by adjList
        res = ''
        q = [  c for c, v in indegree.items() if not v]

        while q:
            node = q.pop()
            res += node
            for nei in adj[node]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        
        return res if len(indegree) == len(res) else ""