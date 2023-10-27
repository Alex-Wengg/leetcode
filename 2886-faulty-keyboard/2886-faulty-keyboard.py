class Solution:
    def finalString(self, s: str) -> str:
        
        curr_seq = []
        
        for i in range(len(s)):
            if s[i] == 'i':
                curr_seq = curr_seq[::-1]
                continue    
            
            curr_seq.append(s[i])                
        return ''.join(curr_seq)