class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabets = [ c for c in s if c.isalpha() ]

        list_s = list(s)
        
        for i, c in enumerate(s):
            if c.isalpha():
                list_s[i] = alphabets.pop(-1)
        return ''.join(list_s)