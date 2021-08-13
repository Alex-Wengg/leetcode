class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashh = {}
        result = 0
        curr = 0 
        start = 0 
        for end in range(len(s)):
            right = s[end]
            if right not in hashh:
                hashh[right] = 0 
            hashh[right] += 1 
            curr += 1 
            
            
            
            while hashh[right] != 1:
                left = s[start]
                
                hashh[left] -= 1
                    
                curr -= 1 
                start += 1 
            
            result = max(result,curr )
        return result