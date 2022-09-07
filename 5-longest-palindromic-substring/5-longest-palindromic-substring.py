class Solution:
    def longestPalindrome(self, s):
        res = ""
        C = 0
        R = 0 
        string = self.updatedString(s)

        LPS = [0 for _ in range(len(string))]
        
        for i in range(len(string)):
            iMirror = 2*C - i
            if R > i:
                LPS[i] = min(R-i, LPS[iMirror])
            else: 
                LPS[i] = 0
            
            try:
                while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                    LPS[i] += 1
            except:
                pass
            
            if i + LPS[i] > R:
                C = i 
                R = i + LPS[i]
        r = max(LPS) 
        c = LPS.index(r)
        return string[c - r : c + r].replace("#","")
    def updatedString(self, string):
        newString = ['#']
        for char in string:
            newString += [char, '#']
        return ''.join(newString)