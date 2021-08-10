class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(x):
            if x == 0:
                return 1
            a = 1
            for i in range(1,x+1):
                a *= i
            return int(a)
        a = helper(m-1)
        b = helper(n-1)

        return helper(m+n-2) //(a*b)