class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        seen = set(brokenLetters)

        text = text.split(" ")
        cnt = 0
        for word in text:
            tempCnt = 1            
            for c in word:
                if c in seen:
                    tempCnt = 0
            cnt += tempCnt 
        return cnt