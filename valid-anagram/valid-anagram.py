class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in smap:
                smap[i] = 0
            smap[i] += 1
        
        
        for i in t:
            if i not  in tmap:
                tmap[i] = 0
            tmap[i] += 1
            
        for i in s:
            
            if not(i in smap) or not(i in tmap):
                return False
            elif smap[i] != tmap[i]:
                return False
        return True
                