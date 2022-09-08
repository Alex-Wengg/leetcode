class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        n = len(s)
        dp_sol = [True] + [False] * n 
        for start in range(n):
            for end in range(start+1, n+1):
                if dp_sol[start] and s[start:end] in wordSet:
                    dp_sol[end] = True

        if not dp_sol[-1]:
            return []
        
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for start in range(n):
            for end in range(start+1, n+1):
                if s[start:end] in wordSet:
                    for sub in dp[start]:
                        dp[end].append(sub + " " + s[start:end])
        return [s[1:] for s in dp[-1]]
        