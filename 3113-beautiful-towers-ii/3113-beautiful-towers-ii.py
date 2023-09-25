class Solution:
    def maximumSumOfHeights(self, A: List[int]) -> int:
        n = len(A)
        def f(A):
            res = [0] * n
            stack = [-1]
            for i in range(n):
                while len(stack) > 1 and A[stack[-1]] > A[i]:
                    j = stack.pop()
                res[i] = res[stack[-1]] + (i - stack[-1]) * A[i]
                stack.append(i)
            return res
        
        return max(pre + suf - a for pre,suf,a in zip(f(A), f(A[::-1])[::-1], A))
