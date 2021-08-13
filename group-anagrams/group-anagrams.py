class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = set()
        for i in strs:
            sets.add(''.join(sorted(i)))
        
        s = list(sets)
        hashh = {}
        for i in s:
            hashh[i] = []
            
        for i in strs:
            word  = (''.join(sorted(i)))
            hashh[word].append(i)
        
        result = []
        for i in hashh:
          
            result.append(hashh[i])
         
        return result 