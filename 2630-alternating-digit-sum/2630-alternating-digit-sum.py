class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        result = 0 
        for i, char in enumerate(n):
            result +=  int(char) if i % 2 == 0 else -1 * int(char)
        return result