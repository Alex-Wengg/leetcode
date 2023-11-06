class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        maxc = 0
        seen = [0] * n

        for idx in range(n):
            if seen[idx] == 0:
                start = idx
                cur_people = idx
                curset = set()

                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = favorite[cur_people]
                
                if cur_people in curset:
                    cursum = len(curset)

                    while start != cur_people:
                        cursum -= 1
                        start = favorite[start]
                    maxc = max(maxc, cursum)
        
        pair = []
        visited = [ 0] * n
        for i in range(n):
            if favorite[favorite[i]] == i and visited[i] == 0:
                pair.append([i, favorite[i]])
                visited[i] = 1
                visited[favorite[i]] = 1
        res = 0
        child = collections.defaultdict(list)
        for i in range(n):
            child[favorite[i]].append(i)
        
        for a, b in pair:
            maxa= 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n +1])
            maxb = 0
            dq = collections.deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, n =dq.popleft()
                maxb = max(maxb, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])
            res += 2 + maxa + maxb
        return max(maxc, res)