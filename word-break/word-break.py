class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dictt = {}
        for i in wordDict:
            if i not in dictt:
                dictt[i] = 0
            dictt[i] += 1 
        
        dp = [ 0 for i in range(len(s)+1)]
        dp[0] = 1
        for i in range(len(s)):
            
            if dp[i]:
                for j in range(i, len(s)):
                    word = s[i:(j+1)]
                    if word in dictt and dp[i]:
                        dp[j+1] = 1
                        
                    
        return dp[-1]
                
                