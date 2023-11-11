
class Solution:
    def minimumTime(self, A: List[int], B: List[int], x: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        
        for j, (b, a) in enumerate(sorted(zip(B, A)), 1):
            for i in range(j, 0, -1):
                dp[i] = max(dp[i], dp[i-1] + i * b + a)
            
        sa, sb = sum(A), sum(B)
        for i in range(n + 1):
            if sb * i + sa - dp[i] <= x:
                return i 
        return -1