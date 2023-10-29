class Solution:
    def isFascinating(self, n: int) -> bool:
        seen_ = "123456789"

        check = str(n) + str(2 * n) + str(3 * n) 
        return seen_ == ''.join(sorted(check))