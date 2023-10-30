class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        return len(s) >= 8 and any(c.islower() for c in s) and any(c.isupper() for c in s) and any(c.isdigit() for c in s) and any(c for c in s if c in "!@#$%^&*()-+") and not(any(s[i] == s[i+1] for i in range(len(s) - 1)))