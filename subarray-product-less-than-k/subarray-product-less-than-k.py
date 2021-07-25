class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0

        ans = 0 
        results = []
        x = 1
        sub = 0
        left = 0
        for right in range(len(nums)):
            x *= nums[right]
           
            while x >= k:
                x /= nums[left]
                left += 1
            ans +=  right - left + 1 
        return ans