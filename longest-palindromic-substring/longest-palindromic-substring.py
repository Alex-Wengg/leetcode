def middle(s, left ,right):
    while 0 <= left and right < len(s)  and s[right] == s[left]:
        left -= 1 
        right += 1
    return right - left -  1

class Solution:
    def longestPalindrome(self, s: str) -> str:        
        start = 0
        end  = 0 
        for i in range(len(s)):
            even = middle(s, i, i)
            odd = middle(s,i, i+1)
            best = max(even, odd)
            
            if best > end-start:
                start = i - (best-1)//2
                end = i + best//2
            
        return s[start:end+1]