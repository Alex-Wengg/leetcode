class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        preWords = {}
        
        words.sort(key = lambda x : len(x))
        for i in range(len(words)):
            if self.dp(words[i], preWords):
                result.append(words[i])
            preWords[words[i]] = 1
        return result
    
    def dp(self,word, dicc):
        if not(dicc):
            return False;
        
        dp = [False for i in range(len(word)+1)]
        
        dp[0] = True
        
        for i in range(1, len(word)+1):
            for j in range(i):
                if not(dp[j]):
                    continue
                if (word[j:i]) in dicc:
                    dp[i] = True
                    break
        return dp[len(word)]