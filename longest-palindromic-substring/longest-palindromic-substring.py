        
def middle(s, left,right):
    while(0<=left and right< len(s) and s[left] == s[right]):
        left -=1
        right +=1
    return (right - left -1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = middle(s, i, i)
            len2 = middle(s, i, i+1)
            bestLen = max(len1,len2)
            
            if (bestLen > end-start):
                start = i - (bestLen-1)//2
                end = i + bestLen//2
        
        return s[start:end+1]
                
