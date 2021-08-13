class Solution:
    def minWindow(self, str1: str, pattern: str) -> str:
        hashh = {}
        for i in pattern:
            if i not in hashh:
                hashh[i] = 0
            hashh[i] += 1 
            
        start = 0 
        match = 0
        head = 0
        tail = len(str1)
        for end in range(len(str1)):
            right = str1[end]
            if right in hashh:
                hashh[right] -= 1
                if hashh[right] >= 0:
                    match += 1 
                    

            
            while match == len(pattern):
                if tail- head +1 >  end - start +1:
                    head = start
                    tail = end
                
                left = str1[start]
                
                if left in hashh:
                   
                    if hashh[left] == 0:
                        match -= 1    
                    hashh[left] += 1
                start += 1 
        if tail ==  len(str1):
            return ""
        return str1[head:tail+1]