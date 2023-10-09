class Solution:
    def alienOrder(self, words):
        # a -> b
        adj = defaultdict(set)
        
        # in-degree construction
        deg = {c: 0 for w in words for c in w}

        # adjList construction
        for i, w1 in enumerate(words[:-1]):
            is_prefix = True
            w2 = words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 == c2: continue
                if c2 not in adj[c1]: deg[c2] += 1
                is_prefix = False

                adj[c1].add(c2)
                break
            if is_prefix == True and len(w1) > len(w2):
                return ""

        res = ''
        # sort by indegree, traversed by adjList
        q = deque([c for c in deg if not deg[c]])
        while q:
            c = q.popleft()
            res += c
            for n in adj[c]:
                deg[n] -= 1
                if not deg[n]: q.append(n)
        return res if len(res) == len(deg) else ''    