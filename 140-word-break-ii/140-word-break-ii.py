class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s] 
        if not s: return []
    
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(s) == len(word):
                res.append(word)
            else:
                restOfResult = self.helper(s[len(word):], wordDict, memo)
                for item in restOfResult:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res