from collections import Counter

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0: return str(n // d)
        
        p, q = map(abs, (n, d))
 
        prefix = ('' if (n > 0) == (d > 0) else '-') + str(p //q) + '.'
        suffix = ''
        remainder = p % q
        index = {}
        
        while remainder not in index:
            index[remainder] = len(suffix)
            suffix += str(remainder * 10 // q)
            remainder = remainder * 10 % q
            if remainder == 0 : return prefix + suffix
 
        return prefix + suffix[:index[remainder]] + '(' + suffix[index[remainder]:] + ')'
 
 