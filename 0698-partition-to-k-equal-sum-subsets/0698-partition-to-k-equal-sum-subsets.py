class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        dp = [ -1 for i in range(1<< 16 + 2)]
        dp[0] = 0

        sum_ = sum(arr)
        if sum_ % k:
            return False
        tar = sum_ // k 

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            for i in range(n):
                if (not(mask & 1 << i) and dp[mask] + arr[i] <= tar):
                    dp[mask | (1 << i)] = (dp[mask] + arr[i]) % tar
        
        return dp[(1 << n) -1 ] == 0
