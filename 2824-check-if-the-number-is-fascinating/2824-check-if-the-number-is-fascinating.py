class Solution:
    def isFascinating(self, n: int) -> bool:
        return "123456789" == ''.join(sorted(str(n) + str(2 * n) + str(3 * n) ))