class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDia = set()
        negDia = set()
        
        res = []
        board = [ ['.']*n  for row in range(n)]
        
        def bfs(r):
            if r == n:
                res.append(1)
            
            for c in range(n):
                if c in col or (r+c) in posDia or (r-c) in negDia:
                    continue
                    
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)

                bfs(r+1)
                
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)

        bfs(0)
        return sum(res)
            