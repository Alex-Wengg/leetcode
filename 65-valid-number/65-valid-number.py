class Solution:
    def isNumber(self, s: str) -> bool:
        
        s = s.strip().lower()
        e_met = False
        dot_met = False
        digit_met = False
        
        for i, char in enumerate(s):
            
            if s[i] in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if dot_met or e_met:
                    return False
                dot_met = True
            elif char == 'e':
                if e_met or not digit_met:
                    return False
                e_met = True
                digit_met = False
            

            elif char.isdigit():
                digit_met = True
            else:
                return False
        return digit_met
            