class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        seen = set()
        i = 0
        ans = 0
        cur = 0

        for j, x in enumerate(nums):
            cur += nums[j]
            
            while j+1-i > k or nums[j] in seen:
                seen.remove(nums[i])
                cur -= nums[i]
                i += 1
            seen.add(x)

            if j+1-i == k:
                ans = max(cur, ans)

        return ans or 0