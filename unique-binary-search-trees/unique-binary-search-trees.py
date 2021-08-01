class Solution:
    def numTrees(self, n: int):
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))