class Solution:
    def romanToInt(self, s: str) -> int:
        sums =0
        d= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
          sums+=(d[s[i]])
          if i+1 < len(s):
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
              sums -=2
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
              sums -=20
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
              sums -=200
        return(sums)