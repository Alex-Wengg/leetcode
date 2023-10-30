class Solution:
    def reformat(self, s: str) -> str:
        a = [ c for c in s if c.isalpha()]
        b = [ c for c in s if c.isdigit()]

        result = []

        if len(a) < len(b):
            a, b = b, a
        if len(a) - len(b) >= 2:
            return ''
        for i in range(min(len(a), len(b))):
            result.append(a[i])
            result.append(b[i])

        if len(a) > len(b):
            result.append(a[-1])
        if len(a) < len(b):
            result.append(b[-1])
        return "".join(result)