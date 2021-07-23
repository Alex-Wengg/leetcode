class Solution:
    def minWindow(self, str1: str, pattern: str) -> str:
    
    
        start, match, substr_start = 0, 0, 0
        substr = { 'start' : 0, 'end' :  len(str1) }
        mapp = {}
            
        for chr in pattern:
            if chr not in mapp:
                mapp[chr] = 0
            mapp[chr] += 1

        # try to extend the range [window_start, window_end]
        for end in range(len(str1)):
            right  = str1[end]
            if right in mapp:
                mapp[right] -= 1
                if mapp[right] >= 0:
                    match += 1
            
            while len(pattern) == match:
                
                if (substr['end'] - substr['start'] + 1) > end - start + 1:
                    substr['end'] = end 
                    substr['start'] = start
                
                left = str1[start] 
                if left in mapp: 
                    if mapp[left] == 0:
                        match -=1 
                    mapp[left] += 1
                start += 1 
        if substr['end'] ==  len(str1):
            return ""
        return str1[substr['start']:(substr['end']+1)]